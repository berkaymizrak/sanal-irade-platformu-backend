from core.models import AbstractModel
from django.conf import settings
from django.db import models
from django.utils.translation import get_language, gettext_lazy as _
from tools.models import District
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.

class Election(TranslatableModel, AbstractModel):
    translations = TranslatedFields(
        name=models.CharField(
            max_length=255,
            verbose_name=_('Name'),
        ),
    )
    start_date = models.DateTimeField(
        verbose_name=_('Start Date'),
        blank=True,
        auto_now=True,
    )
    end_date = models.DateTimeField(
        verbose_name=_('End Date'),
        blank=True,
        auto_now=True,
    )

    class Meta:
        ordering = ('translations__name',)
        verbose_name = _('Election')
        verbose_name_plural = _('Elections')

    def __str__(self):
        return str(
            self.safe_translation_getter(
                'name', language_code=get_language() or settings.LANGUAGE_CODE
            )
        )


class ElectionCandidate(AbstractModel):
    election = models.ForeignKey(
        Election,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Election'),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )
    logo = models.ImageField(
        default='',
        blank=True,
        verbose_name=_('Logo'),
        upload_to='elections/candidates/',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = _('Election Candidate')
        verbose_name_plural = _('Election Candidates')

    def __str__(self):
        return f'{self.name} ({self.election})'


class BallotBox(AbstractModel):
    election = models.ForeignKey(
        Election,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Election'),
    )
    box_number = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Box Number'),
    )
    district = models.ForeignKey(
        District,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('District'),
    )

    class Meta:
        ordering = ('-election__start_date', 'box_number',)
        verbose_name = _('Ballot Box')
        verbose_name_plural = _('Ballot Boxes')

    def __str__(self):
        return f'Box {self.box_number}'


class ElectionResult(AbstractModel):
    candidate = models.ForeignKey(
        ElectionCandidate,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Election Candidate'),
    )
    ballot_box = models.ForeignKey(
        BallotBox,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Ballot Box'),
    )
    votes = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Votes'),
    )

    class Meta:
        ordering = ('votes',)
        verbose_name = _('Election Result')
        verbose_name_plural = _('Election Results')

    def __str__(self):
        return f'{self.candidate} - {self.votes}'


class BallotBoxReport(AbstractModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('User'),
    )
    ballot_box = models.ForeignKey(
        BallotBox,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Ballot Box'),
    )
    report = models.FileField(
        default='',
        blank=True,
        verbose_name=_('Report'),
        upload_to='elections/reports/',
    )
    total_votes = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Total Votes'),
    )
    approved = models.BooleanField(
        default=False,
        verbose_name=_('Approved'),
    )

    class Meta:
        ordering = ('-ballot_box__election__start_date', '-created_date',)
        verbose_name = _('Ballot Box Report')
        verbose_name_plural = _('Ballot Box Reports')

    def __str__(self):
        return f'Report {self.user} ({self.ballot_box}) - {self.ballot_box.election}'


class CandidateReport(AbstractModel):
    ballet_box_report = models.ForeignKey(
        BallotBoxReport,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Ballot Box Report'),
    )
    candidate = models.ForeignKey(
        ElectionCandidate,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Election Candidate'),
    )
    votes = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Votes'),
    )

    class Meta:
        ordering = ('-ballet_box_report', '-created_date',)
        verbose_name = _('Candidate Report')
        verbose_name_plural = _('Candidate Reports')

    def __str__(self):
        return f'Report Line ({self.ballet_box_report})'

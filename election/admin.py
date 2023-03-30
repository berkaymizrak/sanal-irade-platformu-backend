from django.contrib import admin
from election.models import *
from parler.admin import TranslatableAdmin


# Register your models here.


@admin.register(ElectionCandidate)
class ElectionCandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'election', 'logo',)
    list_filter = ('election',)
    search_fields = ('name',)
    list_editable = ()
    autocomplete_fields = ('election',)


class ElectionCandidateInline(admin.TabularInline):
    model = ElectionCandidate
    extra = 0
    autocomplete_fields = ()


@admin.register(Election)
class ElectionAdmin(TranslatableAdmin):
    list_display = ('name', 'language_column', 'start_date', 'end_date',)
    list_filter = ()
    search_fields = ('translations__name',)
    list_editable = ()
    inlines = [ElectionCandidateInline, ]


@admin.register(BallotBox)
class BallotBoxAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'election', 'district',)
    list_filter = ('election',)
    search_fields = ('election__translations__name', 'district__translations__name',)
    list_editable = ()
    autocomplete_fields = ('election', 'district',)


@admin.register(ElectionResult)
class ElectionResultAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'ballot_box', 'votes',)
    list_filter = ('candidate',)
    search_fields = ('candidate__name', 'ballot_box__district__translations__name',)
    list_editable = ()
    autocomplete_fields = ('candidate', 'ballot_box',)


@admin.register(CandidateReport)
class CandidateReportAdmin(admin.ModelAdmin):
    list_display = ('ballot_box_report', 'candidate', 'votes',)
    list_filter = ('ballot_box_report__approved', 'candidate__election', 'candidate',)
    search_fields = (
        'candidate__name',
        'ballot_box_report__ballot_box__district__translations__name',
        'ballot_box_report__user__first_name',
        'ballot_box_report__user__last_name',
        'ballot_box_report__user__email',
    )
    list_editable = ()
    autocomplete_fields = ('ballot_box_report', 'candidate',)


class CandidateReportInline(admin.TabularInline):
    model = CandidateReport
    extra = 0
    autocomplete_fields = ('candidate',)


@admin.register(BallotBoxReport)
class BallotBoxReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'ballot_box', 'total_votes', 'approved',)
    list_filter = ('approved', 'ballot_box__election',)
    search_fields = ('ballot_box__election',)
    list_editable = ()
    autocomplete_fields = ('user', 'ballot_box',)
    inlines = [CandidateReportInline, ]

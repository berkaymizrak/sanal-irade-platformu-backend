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


class ElectionCandidateInline(admin.StackedInline):
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


@admin.register(ElectionResult)
class ElectionResultAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'ballot_box', 'votes',)
    list_filter = ('candidate',)
    search_fields = ('candidate__name', 'ballot_box__district__translations__name',)
    list_editable = ()


@admin.register(CandidateReport)
class CandidateReportAdmin(admin.ModelAdmin):
    list_display = ('ballet_box_report', 'candidate', 'votes',)
    list_filter = ('candidate',)
    search_fields = (
        'candidate__name',
        'ballet_box_report__ballot_box__district__translations__name',
        'ballet_box_report__user__first_name',
        'ballet_box_report__user__last_name',
        'ballet_box_report__user__email',
    )
    list_editable = ()


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
    inlines = [CandidateReportInline, ]

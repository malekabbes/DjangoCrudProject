from django.contrib import admin
from.models import *
# Register your models here.
class ParticipationAdmin(admin.TabularInline):
    model=Event_Participation
    extra=1

@admin.register(Event) 
class EventAdmin(admin.ModelAdmin):
    list_display=('title','description','nbe_participant','state','event_date','update_date','organizer')
# admin.site.register(Event,EventAdmin)
    list_per_page=2
    list_filter=('title','event_date','nbe_participant')
    fieldsets=[
        ('A propos', {
        "fields":(
        'title',
        'description',
        'image',
        'state'
        )
        }),
        ('Date',{
        "fields":(
        "event_date",
        "creation_date",
        "update_date",
        )
        }),
        ('Personnel',{
        "fields":(
        "organizer",
        )
        })
    ]
    readonly_fields=["creation_date","update_date"]
    inlines=(ParticipationAdmin,)
@admin.register(Person)
class SearchPerson(admin.ModelAdmin):
    search_fields=['username']
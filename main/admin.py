from django.contrib import admin

from main.models import *


# class AircraftsDataAdmin(admin.ModelAdmin):
#     pass
#
#
# class AirportsDataAdmin(admin.ModelAdmin):
#     pass
#
#
# class BoardingPassesAdmin(admin.ModelAdmin):
#     pass
#
#
# class BookingsAdmin(admin.ModelAdmin):
#     pass
#
#
# class FlightsAdmin(admin.ModelAdmin):
#     pass
#
#
# class SeatsAdmin(admin.ModelAdmin):
#     pass
#
#
# class TicketFlightsAdmin(admin.ModelAdmin):
#     pass
#
#
# class TicketsAdmin(admin.ModelAdmin):
#     pass


admin.site.register(AircraftsData)
admin.site.register(AirportsData)
admin.site.register(BoardingPasses)
admin.site.register(Bookings)
admin.site.register(Flights)
admin.site.register(Seats)
admin.site.register(TicketFlights)
admin.site.register(Tickets)

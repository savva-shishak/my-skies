from django.http import JsonResponse
from django.db import connection
from .models import Flights, AirportsData, Tickets, AircraftsData


def get_numbers_and_flights(_):
    with connection.cursor() as cursor:
        cursor.execute("""
                    select 
                        f.flight_no, 
                        a.model->>'ru',
                        arr.airport_name->>'ru',
                        dep.airport_name->>'ru'
                    from 
                        flights f 
                        join aircrafts_data a on a.aircraft_code = f.aircraft_code 
                        join airports_data arr on arr.airport_code = f.arrival_airport
                        join airports_data dep on dep.airport_code = f.departure_airport 
                        
                        group by f.flight_no, a.aircraft_code, arr.airport_code, dep.airport_code
                        limit 10;
                """)

        return JsonResponse({
            "flights": Flights.objects.count(),
            "airports": AirportsData.objects.count(),
            "tickets": Tickets.objects.count(),
            "aircrafts": AircraftsData.objects.count(),

            "flights_list": cursor.fetchall()
    })


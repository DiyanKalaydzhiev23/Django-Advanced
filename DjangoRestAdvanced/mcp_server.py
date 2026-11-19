import os
import django
from fastmcp import FastMCP

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoRestBasicsExercise.settings")
django.setup()

from django.db.models import Count, Min, Max
from garage_api.models import Car

mcp = FastMCP("garage")

@mcp.tool()
async def car_stats() -> dict:
    return await Car.objects.aaggregate(
        total_cars=Count('id'),
        oldest_car=Min('year'),
        newest_car=Max('year')
    )

if __name__ == "__main__":
    mcp.run()

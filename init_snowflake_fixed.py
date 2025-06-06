from snowflake_utils import SnowflakeManager
import pandas as pd
from pathlib import Path


def init_snowflake():
    """Initialize Snowflake database with all our data"""
    # Initialize Snowflake manager
    sf_manager = SnowflakeManager()

    # Create tables
    if not sf_manager.create_tables():
        print("Failed to create tables")
        return

    # Load data from CSV files
    assets_path = Path("assets")

    # 1. Load art forms data
    art_forms_df = pd.read_csv(assets_path / "art_forms.csv")
    art_forms_df = art_forms_df.rename(columns={
        'art_form_name': 'NAME',
        'region': 'REGION',
        'style': 'DESCRIPTION',
        'description': 'HISTORY',
        'image_path': 'IMAGE_URL'
    })
    sf_manager.load_data_from_csv(art_forms_df, "art_forms")

    # 2. Load cultural events data
    events_df = pd.read_csv(assets_path / "festivals_kaggle.csv")
    events_df = events_df.rename(columns={
        'Festival name': 'NAME',
        'Date': 'DATE',
        'Year': 'YEAR'
    })
    events_df['LOCATION'] = 'India'
    events_df['DESCRIPTION'] = events_df['NAME']
    events_df['TYPE'] = 'Festival'
    events_df['REGION'] = 'All India'
    sf_manager.load_data_from_csv(events_df, "cultural_events")

    # 3. Load heritage sites data
    heritage_df = pd.read_csv(
        assets_path / "WORLD HERITAGE SITES 2024 UPDATED.csv")
    heritage_df = heritage_df.rename(columns={
        'name': 'NAME',
        'location': 'LOCATION',
        'latitude': 'LATITUDE',
        'longitude': 'LONGITUDE',
        'description': 'DESCRIPTION',
        'historical_significance': 'HISTORICAL_SIGNIFICANCE',
        'image_url': 'IMAGE_URL'
    })
    sf_manager.load_data_from_csv(heritage_df, "heritage_sites")

    # 4. Load tourism statistics
    tourism_df = pd.read_csv(assets_path / "foreignVisit.csv")
    tourism_df = tourism_df.rename(columns={
        'year': 'YEAR',
        'state': 'STATE',
        'foreign_visitors': 'FOREIGN_VISITORS',
        'domestic_visitors': 'DOMESTIC_VISITORS',
        'growth_rate': 'GROWTH_RATE'
    })
    sf_manager.load_data_from_csv(tourism_df, "tourism_statistics")

    # 5. Load festival calendar data
    festival_calendar_df = pd.read_csv(assets_path / "festivalCalendar.csv")
    festival_calendar_df = festival_calendar_df.rename(columns={
        'Festival': 'NAME',
        'Date': 'DATE',
        'Description': 'DESCRIPTION',
        'Region': 'REGION'
    })
    festival_calendar_df['TYPE'] = 'Festival'
    sf_manager.load_data_from_csv(festival_calendar_df, "festival_calendar")

    # 6. Load places data
    places_df = pd.read_csv(assets_path / "places.csv")
    places_df = places_df.rename(columns={
        'name': 'NAME',
        'description': 'DESCRIPTION',
        'location': 'LOCATION',
        'type': 'TYPE',
        'image_url': 'IMAGE_URL'
    })
    sf_manager.load_data_from_csv(places_df, "tourist_places")

    # 7. Load country-wise visitor statistics
    country_visitors_df = pd.read_csv(
        assets_path / "Country Quater Wise Visitors.csv")
    country_visitors_df = country_visitors_df.rename(columns={
        'Country': 'COUNTRY',
        'Quarter': 'QUARTER',
        'Year': 'YEAR',
        'Visitors': 'VISITOR_COUNT'
    })
    sf_manager.load_data_from_csv(country_visitors_df, "country_visitors")

    print("Successfully initialized Snowflake database with all data!")

    # Close connection
    sf_manager.close()


if __name__ == "__main__":
    init_snowflake()

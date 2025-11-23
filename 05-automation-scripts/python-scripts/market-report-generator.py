#!/usr/bin/env python3
"""
Market Report Generator
Automates the creation of weekly market reports from MLS data

Usage:
    python market-report-generator.py --input data.csv --output weekly-report.md

Requirements:
    - pandas
    - python-dateutil

Install:
    pip install pandas python-dateutil
"""

import pandas as pd
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import sys

class MarketReportGenerator:
    """Generates formatted market reports from MLS data"""

    def __init__(self, data_file):
        """
        Initialize the generator with data file

        Args:
            data_file (str): Path to CSV file with MLS data
        """
        try:
            self.df = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            print(f"Error: File '{data_file}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading data: {e}")
            sys.exit(1)

    def validate_data(self):
        """Ensure required columns exist in the data"""
        required_columns = [
            'ListPrice', 'Status', 'BedsTotal', 'BathsTotal',
            'ListingDate', 'SqFtTotal', 'DaysOnMarket'
        ]

        missing = [col for col in required_columns if col not in self.df.columns]
        if missing:
            print(f"Warning: Missing columns: {missing}")
            print(f"Available columns: {list(self.df.columns)}")

    def filter_week(self, week_ending_date):
        """
        Filter data for the specified week

        Args:
            week_ending_date (datetime): End date of the week to analyze

        Returns:
            DataFrame: Filtered data for the week
        """
        week_start = week_ending_date - timedelta(days=7)

        # Convert ListingDate to datetime if it's not already
        self.df['ListingDate'] = pd.to_datetime(self.df['ListingDate'])

        mask = (self.df['ListingDate'] >= week_start) & (self.df['ListingDate'] <= week_ending_date)
        return self.df[mask]

    def calculate_stats(self, df):
        """
        Calculate market statistics

        Args:
            df (DataFrame): Data to analyze

        Returns:
            dict: Dictionary of calculated statistics
        """
        stats = {
            'total_listings': len(df),
            'median_price': df['ListPrice'].median(),
            'average_price': df['ListPrice'].mean(),
            'min_price': df['ListPrice'].min(),
            'max_price': df['ListPrice'].max(),
            'avg_sqft': df['SqFtTotal'].mean(),
            'avg_price_per_sqft': (df['ListPrice'] / df['SqFtTotal']).mean(),
            'avg_days_on_market': df['DaysOnMarket'].mean(),
            'median_days_on_market': df['DaysOnMarket'].median(),
        }

        # Property type breakdown
        if 'PropertyType' in df.columns:
            stats['by_type'] = df.groupby('PropertyType').agg({
                'ListPrice': ['count', 'mean'],
                'SqFtTotal': 'mean'
            }).round(2)

        return stats

    def generate_report(self, week_ending_date, output_file=None):
        """
        Generate complete market report

        Args:
            week_ending_date (datetime): End date of week to report on
            output_file (str, optional): Path to save report

        Returns:
            str: Formatted market report in Markdown
        """
        # Filter data for the week
        week_data = self.filter_week(week_ending_date)

        if len(week_data) == 0:
            print(f"Warning: No data found for week ending {week_ending_date}")
            return None

        # Calculate statistics
        stats = self.calculate_stats(week_data)

        # Generate report
        report = self._format_report(week_ending_date, stats, week_data)

        # Save if output file specified
        if output_file:
            Path(output_file).write_text(report)
            print(f"Report saved to: {output_file}")

        return report

    def _format_report(self, week_ending_date, stats, data):
        """
        Format the report in Markdown

        Args:
            week_ending_date (datetime): End date of the week
            stats (dict): Calculated statistics
            data (DataFrame): Raw data for the week

        Returns:
            str: Formatted Markdown report
        """
        report = f"""# Weekly Market Report

## Report Information
- **Week Ending**: {week_ending_date.strftime('%B %d, %Y')}
- **Report Generated**: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
- **Data Points**: {len(data)} listings analyzed

---

## Executive Summary

This week saw {stats['total_listings']} new listings with a median price of ${stats['median_price']:,.0f}.
The average price per square foot was ${stats['avg_price_per_sqft']:.2f}, and homes are spending an
average of {stats['avg_days_on_market']:.0f} days on the market.

---

## New Listings

### Overview
- **Total New Listings**: {stats['total_listings']}
- **Average List Price**: ${stats['average_price']:,.0f}
- **Median List Price**: ${stats['median_price']:,.0f}
- **Price Range**: ${stats['min_price']:,.0f} - ${stats['max_price']:,.0f}

### Pricing Metrics
- **Average $/SqFt**: ${stats['avg_price_per_sqft']:.2f}
- **Average Square Footage**: {stats['avg_sqft']:,.0f} sq ft

### Time on Market
- **Average DOM**: {stats['avg_days_on_market']:.0f} days
- **Median DOM**: {stats['median_days_on_market']:.0f} days

---

## Property Type Breakdown

"""
        # Add property type breakdown if available
        if 'by_type' in stats:
            report += "| Property Type | Count | Avg Price | Avg SqFt |\n"
            report += "|---------------|-------|-----------|----------|\n"

            for prop_type, row in stats['by_type'].iterrows():
                count = int(row[('ListPrice', 'count')])
                avg_price = row[('ListPrice', 'mean')]
                avg_sqft = row[('SqFtTotal', 'mean')]
                report += f"| {prop_type} | {count} | ${avg_price:,.0f} | {avg_sqft:,.0f} |\n"

        report += """

---

## Notable Listings

"""
        # Add top 5 highest-priced listings
        top_listings = data.nlargest(5, 'ListPrice')
        for idx, listing in top_listings.iterrows():
            address = listing.get('Address', 'Address not available')
            price = listing['ListPrice']
            beds = listing.get('BedsTotal', 'N/A')
            baths = listing.get('BathsTotal', 'N/A')
            sqft = listing.get('SqFtTotal', 'N/A')

            report += f"- **{address}** - ${price:,.0f} - {beds} bed / {baths} bath - {sqft:,.0f} sq ft\n"

        report += """

---

## Analysis

### Market Trends
*[Add your analysis of trends based on the numbers above]*

### For Buyers
*[Add buyer-specific insights]*

### For Sellers
*[Add seller-specific insights]*

---

## Data Sources

- **Source**: MLS Data Export
- **Date Range**: {week_start} to {week_end}
- **Property Types**: All residential
- **Status**: Active listings

---

*Report generated automatically using Claude Code Market Report Generator*
*For questions or custom analysis, contact [Your Name]*
""".format(
            week_start=(week_ending_date - timedelta(days=7)).strftime('%B %d, %Y'),
            week_end=week_ending_date.strftime('%B %d, %Y')
        )

        return report

    def compare_weeks(self, current_week, previous_week):
        """
        Compare two weeks and identify trends

        Args:
            current_week (datetime): End date of current week
            previous_week (datetime): End date of previous week

        Returns:
            dict: Comparison statistics
        """
        current_data = self.filter_week(current_week)
        previous_data = self.filter_week(previous_week)

        current_stats = self.calculate_stats(current_data)
        previous_stats = self.calculate_stats(previous_data)

        comparison = {
            'listings_change': current_stats['total_listings'] - previous_stats['total_listings'],
            'listings_pct_change': ((current_stats['total_listings'] - previous_stats['total_listings']) /
                                   previous_stats['total_listings'] * 100 if previous_stats['total_listings'] > 0 else 0),
            'price_change': current_stats['median_price'] - previous_stats['median_price'],
            'price_pct_change': ((current_stats['median_price'] - previous_stats['median_price']) /
                                previous_stats['median_price'] * 100 if previous_stats['median_price'] > 0 else 0),
            'dom_change': current_stats['avg_days_on_market'] - previous_stats['avg_days_on_market'],
        }

        return comparison


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description='Generate weekly market reports from MLS data'
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to input CSV file with MLS data'
    )
    parser.add_argument(
        '--output', '-o',
        help='Path to output Markdown file (optional)'
    )
    parser.add_argument(
        '--date', '-d',
        help='Week ending date (YYYY-MM-DD). Defaults to today.'
    )
    parser.add_argument(
        '--compare',
        action='store_true',
        help='Compare with previous week'
    )

    args = parser.parse_args()

    # Parse date
    if args.date:
        try:
            week_ending = datetime.strptime(args.date, '%Y-%m-%d')
        except ValueError:
            print("Error: Date must be in YYYY-MM-DD format")
            sys.exit(1)
    else:
        week_ending = datetime.now()

    # Create generator
    generator = MarketReportGenerator(args.input)

    # Generate report
    report = generator.generate_report(week_ending, args.output)

    if report:
        print("\n" + "="*50)
        print("MARKET REPORT GENERATED")
        print("="*50)
        if not args.output:
            print(report)

    # Compare weeks if requested
    if args.compare:
        previous_week = week_ending - timedelta(days=7)
        comparison = generator.compare_weeks(week_ending, previous_week)

        print("\n" + "="*50)
        print("WEEK-OVER-WEEK COMPARISON")
        print("="*50)
        print(f"New Listings: {comparison['listings_change']:+d} ({comparison['listings_pct_change']:+.1f}%)")
        print(f"Median Price: ${comparison['price_change']:+,.0f} ({comparison['price_pct_change']:+.1f}%)")
        print(f"Days on Market: {comparison['dom_change']:+.1f} days")


if __name__ == '__main__':
    main()


"""
EXAMPLE USAGE:

1. Basic report generation:
   python market-report-generator.py --input mls-data.csv --output weekly-report.md

2. Generate for specific date:
   python market-report-generator.py --input mls-data.csv --date 2024-11-22

3. With week-over-week comparison:
   python market-report-generator.py --input mls-data.csv --output report.md --compare

4. View in console without saving:
   python market-report-generator.py --input mls-data.csv


EXPECTED CSV FORMAT:

Your CSV file should have these columns (minimum):
- ListPrice: Listing price (numeric)
- Status: Listing status (Active, Pending, Sold, etc.)
- BedsTotal: Number of bedrooms (numeric)
- BathsTotal: Number of bathrooms (numeric)
- ListingDate: Date listed (YYYY-MM-DD)
- SqFtTotal: Square footage (numeric)
- DaysOnMarket: Days on market (numeric)
- PropertyType: Type of property (optional)
- Address: Property address (optional, for notable listings)


CUSTOMIZATION:

You can customize this script by:
1. Modifying the _format_report() method to change report structure
2. Adding new statistical calculations in calculate_stats()
3. Including additional data fields from your MLS
4. Changing the markdown formatting to match your brand


AUTOMATION:

Run this script weekly via cron job or scheduled task:

On Mac/Linux (cron):
0 9 * * 1 /path/to/python market-report-generator.py --input /path/to/data.csv --output /path/to/report.md

On Windows (Task Scheduler):
Create a task that runs weekly and executes:
C:\\Python\\python.exe C:\\path\\to\\market-report-generator.py --input C:\\data\\mls.csv --output C:\\reports\\weekly.md


INTEGRATION WITH CLAUDE CODE:

After generating the report, use Claude Code to:
1. Review and add analysis
2. Generate social media posts from the data
3. Create email newsletter
4. Identify noteworthy trends for video content

Example:
"Claude Code, read the market report I just generated and create 3 social media posts
highlighting the most interesting trends for buyers and sellers."
"""

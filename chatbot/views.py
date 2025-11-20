import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Excel once on server start
excel_file = 'data/real_estate.xlsx'
df = pd.read_excel(excel_file)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

@api_view(['GET'])
def analyze_area(request):
    area = request.GET.get('area', None)
    if not area:
        return Response({"error": "Please provide an area parameter"}, status=400)

    filtered_df = df[df['final_location'].str.lower() == area.lower()]
    if filtered_df.empty:
        return Response({"error": "No data found for this area"}, status=404)

    # CHART DATA
    chart_data = (
        filtered_df.groupby('year')[['total_sales_-_igr', 'total_sold_-_igr']]
        .sum()
        .rename(columns={'total_sales_-_igr': 'total_sales', 'total_sold_-_igr': 'total_sold'})
        .reset_index()
        .to_dict(orient='records')
    )

    # TABLE DATA
    table_data = filtered_df.to_dict(orient='records')

    # --- LLM SUMMARY ---
    prompt = f"""
    You are a real estate analyst. Analyze the dataset for area '{area}'.
    Total sales and total units sold are given per year.

    Here is the data:
    {chart_data}

    Give a short professional real estate summary in 3-4 lines only.
    """

    try:
        client = openai.OpenAI()  # NEW

        response = client.chat.completions.create(
            model="gpt-4o-mini",    # Best choice with free credits
            messages=[
                {"role": "system", "content": "You are a professional real estate analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        ai_summary = response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)
        ai_summary = "LLM summary could not be generated."


    return Response({
        "summary": ai_summary,
        "chart_data": chart_data,
        "table_data": table_data
    })

@api_view(['GET'])
def download_data(request):
    area = request.GET.get('area', None)
    if not area:
        return Response({"error": "Please provide an area parameter"}, status=400)

    # Filter data
    filtered_df = df[df['final_location'].str.lower() == area.lower()]
    if filtered_df.empty:
        return Response({"error": "No data found for this area"}, status=404)

    # Create Excel for download
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{area}_data.xlsx"'

    filtered_df.to_excel(response, index=False)  # Export data to Excel

    return response
import pandas as pd
import dash
import turbo_dash as td

from app import app
from config import STATES_PATH, LOGO_PATH


df = pd.read_csv(STATES_PATH)
# print(df.columns.values)
# ['date', 'state', 'positive', 'negative', 'pending',
#        'hospitalizedCurrently', 'hospitalizedCumulative',
#        'inIcuCurrently', 'inIcuCumulative', 'onVentilatorCurrently',
#        'onVentilatorCumulative', 'recovered', 'hash', 'dateChecked',
#        'death', 'hospitalized', 'total', 'totalTestResults', 'posNeg',
#        'fips', 'deathIncrease', 'hospitalizedIncrease',
#        'negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease',
#        'population', 'positive_test_rate', 'pct_of_population_tested',
#        'pct_of_population_positive', 'simple_death_rate',
#        'inferred_positive', 'hidden_positive',
#        'pct_of_population_inferred_positive',
#        'pct_of_population_hidden_positive']


list_of_inputs = [
    td.TurboInput(
        output_id_list=['totalTestResults-line', 'pct_of_population_tested-line', 'pct_of_population_tested-violin'],
        input_type='Dropdown',
        df=df,
        value_column='state',
        turbo_filter_object=td.TurboFilter(
            input_component_id='state-filter',
            filter_input_property_list=['value'],
            lambda_function_list=[
                lambda dataframe, value: dataframe[dataframe['state'] == value]
            ],
        ),
        input_label_class_name='sidebar-label',
    ),
]

list_of_outputs = [
    td.TurboOutput(
        output_component_id='totalTestResults-line',
        output_component_property='figure',
        output_type='line',
        df=df,
        x='date',
        y='totalTestResults',
        color='state',
        template='seaborn',
        turbo_input_list=list_of_inputs
    ),
    td.TurboOutput(
        output_component_id='pct_of_population_tested-line',
        output_component_property='figure',
        output_type='line',
        df=df,
        x='date',
        y='pct_of_population_tested',
        color='state',
        template='seaborn',
        turbo_input_list=list_of_inputs
    ),
    td.TurboOutput(
        output_component_id='pct_of_population_tested-violin',
        output_component_property='figure',
        output_type='violin',
        df=df[df['date'] == '2020-04-08'],
        # x='date',
        y='pct_of_population_tested',
        # color='state',
        template='seaborn',
        turbo_input_list=list_of_inputs
    ),
]

turbo = td.turbo_dash(
    app_to_callback=app,
    list_of_inputs=list_of_inputs,
    list_of_outputs=list_of_outputs,
    layout_template='turbo',
    turbo_header_logo_file_path=LOGO_PATH,
    turbo_header_links_list=[
        {'href': '/testing', 'text': 'Testing', 'link_class_name': 'header-link-current'},
        {'href': '/positives', 'text': 'Positives'},
        {'href': '/deaths', 'text': 'Deaths'},
    ],
)

layout = turbo.layout
turbo.callbacks

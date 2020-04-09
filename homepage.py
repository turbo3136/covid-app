from app import app
from turbo_dash import turbo_dash

from config import LOGO_PATH


td = turbo_dash(
    app_to_callback=app,
    layout_template='homepage',
    turbo_header_logo_file_path=LOGO_PATH,
    turbo_header_links_list=[
        {'href': '/testing', 'text': 'Testing'},
        {'href': '/positives', 'text': 'Positives'},
        {'href': '/deaths', 'text': 'Deaths'},
    ],
    turbo_img_link=LOGO_PATH,
)

layout = td.layout
td.callbacks

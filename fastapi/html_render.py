from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from jinja2 import Template

html = """
    <html>
        <head>
            <title>this is title</title>
        </head>
        <li>
            {{ name }}
        </li>
    </html>
    """

template = Template(html)

router = APIRouter(prefix="/responses", tags=["response"])


@router.get("/html_sample", response_class=HTMLResponse)
def html_return():
    html_response = template.render(name="HELLO WORLD")
    return html_response

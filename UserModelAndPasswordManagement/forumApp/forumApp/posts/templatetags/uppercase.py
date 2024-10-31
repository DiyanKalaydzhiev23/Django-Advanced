# Register an instance of Library to register custom template tags
from django import template
from django.template import Node

register = template.Library()


# Define a custom Node class for the 'uppercase' tag
class UppercaseNode(Node):
    def __init__(self, nodelist):
        # nodelist is the content between the custom opening and closing tags
        self.nodelist = nodelist

    def render(self, context):
        # Render the content between the tags using the current context
        output = self.nodelist.render(context)
        # Convert the rendered content to uppercase before returning it
        return output.upper()


# Register a custom template tag named "uppercase"
@register.tag(name="uppercase")
def do_uppercase(parser, token):
    # Parse everything between {% uppercase %} and {% enduppercase %}
    nodelist = parser.parse(('enduppercase',))
    # Remove the 'enduppercase' token from the parsing queue
    parser.delete_first_token()
    # Return an instance of the custom UppercaseNode with the parsed nodelist
    return UppercaseNode(nodelist)
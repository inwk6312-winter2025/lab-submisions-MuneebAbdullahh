
from jinja2 import Template

# Define the context for rendering the template
interface_data = {
            'description': 'Uplink to core switch',
                'vlan': 100
                }

# Read the template file
with open('template-task3.j2', 'r') as f:
        template_content = f.read()

# Create a Jinja template from the file content
        template = Template(template_content)

        # Render the template with context data
        output = template.render(interface=interface_data)

        # Print or save the rendered configuration
        print(output)

        # Optionally, write the output to a file
        with open('generated_config.txt', 'w') as f:
                f.write(output)


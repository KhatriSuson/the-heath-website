from graphviz import Digraph

def generate_use_case_diagram():
    # Initialize the diagram
    diagram = Digraph('Hospital Management System', format='png')
    diagram.attr(rankdir='LR')  # Left to right layout

    # Define actors
    diagram.node('Patient', shape='ellipse', color='lightblue', style='filled', fontname='Arial')
    diagram.node('Admin', shape='ellipse', color='lightgreen', style='filled', fontname='Arial')
    diagram.node('Doctor', shape='ellipse', color='orange', style='filled', fontname='Arial')

    # Define use cases
    diagram.node('UC1', label='Manage Patient Records', shape='ellipse')
    diagram.node('UC2', label='Schedule Appointments', shape='ellipse')
    diagram.node('UC3', label='Send Notifications', shape='ellipse')
    diagram.node('UC4', label='Generate Billing and Payments', shape='ellipse')
    diagram.node('UC5', label='Generate Reports', shape='ellipse')
    diagram.node('UC6', label='Manage Roles and Access', shape='ellipse')

    # Connect actors to use cases
    diagram.edge('Patient', 'UC2')
    diagram.edge('Patient', 'UC3')
    diagram.edge('Admin', 'UC1')
    diagram.edge('Admin', 'UC6')
    diagram.edge('Doctor', 'UC1')
    diagram.edge('Doctor', 'UC5')

    # Save diagram to a file
    file_path = 'hospital_management_use_case_diagram'
    diagram.render(file_path, cleanup=True)
    print(f"Use Case Diagram generated and saved as '{file_path}.png'.")

# Generate the Use Case Diagram
generate_use_case_diagram()

def validate_data(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")
    return True

def process(element):
    # Assuming some kind of processing is required on the element
    # Placeholder for processing logic, for instance:
    return element * 2  # Example processing logic, this should be replaced by actual logic

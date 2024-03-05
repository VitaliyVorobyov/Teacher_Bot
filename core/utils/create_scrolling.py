async def scrolling(content: list, start: int, request):
    if start > len(content):
        start = 1
    if start < 1:
        start = len(content)
    content_dict = {x: y for x, y in enumerate([x['file_to_description_id'] for x in content], start=1)}
    first_content = content_dict.get(start)
    file_to_description = await request.get_file_to_description(first_content)
    scroll_data = [start, len(content_dict)]
    row_id = file_to_description[0]['row_id']
    description_id = file_to_description[0]['description_id']
    description = await request.get_description(description_id)
    file = await request.get_file(row_id)
    return scroll_data, file, description

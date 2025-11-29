import re

def parse_roadmap(text):
    """
    Parses roadmap text into a structured list of tasks with timeframes.
    
    Returns:
        list[dict]: A list of parsed items. Each item contains:
            - type: "timeframe" or "task"
            - label: (for timeframe) e.g., "Week 1"
            - granularity: (for timeframe) "month", "week", "day", "hour"
            - parent_label: (for timeframe) label of the parent timeframe
            - timeframe_label: (for task) which timeframe it belongs to
            - title: (for task) task text
    """
    lines = text.split('\n')
    
    # Context trackers
    current_month = None
    current_week = None
    current_day = None
    current_hour = None
    
    parsed_data = []
    
    # Regex patterns
    # Case insensitive matching for headings
    re_month = re.compile(r'^(month\s*\d+.*)', re.IGNORECASE)
    re_week = re.compile(r'^(week\s*\d+.*)', re.IGNORECASE)
    re_day = re.compile(r'^(day\s*\d+.*)', re.IGNORECASE)
    re_hour = re.compile(r'^(hour\s*\d+.*)', re.IGNORECASE)
    
    # Task bullets: -, *, •, or numbered 1.
    re_task = re.compile(r'^(\s*[-*•]|\s*\d+\.)\s*(.*)')

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for headings (Hierarchy: Month > Week > Day > Hour)
        
        # Month
        m_match = re_month.match(line)
        if m_match:
            label = m_match.group(1)
            current_month = label
            current_week = None
            current_day = None
            current_hour = None
            parsed_data.append({
                "type": "timeframe",
                "label": label,
                "granularity": "month",
                "parent_label": None
            })
            continue
            
        # Week
        w_match = re_week.match(line)
        if w_match:
            label = w_match.group(1)
            current_week = label
            current_day = None
            current_hour = None
            parsed_data.append({
                "type": "timeframe",
                "label": label,
                "granularity": "week",
                "parent_label": current_month
            })
            continue
            
        # Day
        d_match = re_day.match(line)
        if d_match:
            label = d_match.group(1)
            current_day = label
            current_hour = None
            parsed_data.append({
                "type": "timeframe",
                "label": label,
                "granularity": "day",
                "parent_label": current_week or current_month
            })
            continue
            
        # Hour
        h_match = re_hour.match(line)
        if h_match:
            label = h_match.group(1)
            current_hour = label
            parsed_data.append({
                "type": "timeframe",
                "label": label,
                "granularity": "hour",
                "parent_label": current_day or current_week or current_month
            })
            continue
            
        # Check for Task
        t_match = re_task.match(line)
        if t_match:
            task_text = t_match.group(2).strip()
            
            # Determine most specific context
            timeframe_label = "Unassigned"
            granularity = "generic"
            
            if current_hour:
                timeframe_label = current_hour
                granularity = "hour"
            elif current_day:
                timeframe_label = current_day
                granularity = "day"
            elif current_week:
                timeframe_label = current_week
                granularity = "week"
            elif current_month:
                timeframe_label = current_month
                granularity = "month"
            
            # If unassigned, we might want to create a generic timeframe if not exists
            # But for simplicity, we'll handle "Unassigned" in the DB saver or UI
            
            parsed_data.append({
                "type": "task",
                "title": task_text,
                "timeframe_label": timeframe_label,
                "granularity": granularity
            })
            continue
            
    return parsed_data

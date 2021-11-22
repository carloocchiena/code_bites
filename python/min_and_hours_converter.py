def min_to_hours(minutes):
    """Convert minutes to hours
    
    int: minutes
    
    return: hours and minutes
    
    """
    if type(minutes) == int:
        hours = round(minutes//60)
        return f"{minutes} minutes are equal to {hours} hours and {minutes % 60} minutes."
    else:
        return "You must insert an integer value"
      
def hours_to_min(hours):
  """Convert hours to minutes

  float: hours

  return: minutes
  """
  if type(hours) == int or type(hours) == float:
      residual = hours - round(hours)
      minutes = round(hours) * 60
      minutes_residual = round (60 * residual, 2)
      total_minutes = minutes + minutes_residual
      return f"{hours} hours are equal to {total_minutes} minutes."
  else:
      return "You must insert a float or integer value"
      

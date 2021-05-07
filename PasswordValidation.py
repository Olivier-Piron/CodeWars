# Regex Password Validation

# ^              Start line
# (?=.*?[a-z])   At least one lowercase letter
# (?=.*?[A-Z])   At least one uppercase letter
# (?=.*\d)       At least one digit
# [^\W_]         Only alphanumeric
# {6,}           At least 6 characters long
# $              End line 

regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"


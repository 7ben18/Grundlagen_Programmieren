def formated_time(seconds):
    temp = '{},{},{},{},{}'.format(
        seconds // 31536000,
        seconds // 86400 % 24,
        seconds // 86400 // 24 % 60,
        seconds // 86400 // 24 // 60 % 60,
        seconds // 86400 // 24 // 60 // 60 % 60)

    return temp


print(formated_time(86400))

import user

if user.belhard_student:
    status = "I am not a Belhard student"
else:
    status = "I am a Belhard student"

print(f"My name is {user.name} {user.surname}\n"
      f"I am {user.age} years old\n"
      f"{status}")
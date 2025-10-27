# test_user_profile.py - Нэгж туршилт (TDD аргаар)
def test_user_profile_creation():
 # Туршилтын өгөгдөл
 user = User("Бат", "бат@example.com")
 profile = UserProfile(user, "Зураг", "Би веб хөгжүүлэгч")

 assert profile.user.name == "Бат"
 assert profile.avatar == "Зураг"
 assert profile.bio == "Би веб хөгжүүлэгч"

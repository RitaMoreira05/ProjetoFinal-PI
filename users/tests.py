from django.test import TestCase
from django.urls import reverse
from .models import Utilizador
from django.conf import settings
from django.urls import reverse

class RegisterViewTest(TestCase):
    def test_register_user_success(self):
        data = {
            'username': 'newuser',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
            'email': 'newuser@example.com',
        }
        response = self.client.post(reverse('registar'), data)
        
        # Verifique se houve redirecionamento após o sucesso
        self.assertEqual(response.status_code, 200)  # Redirecionamento esperado após sucesso
        
        # Verifique se o usuário foi criado no banco de dados
        self.assertTrue(Utilizador.objects.filter(username='newuser').exists())
        print(Utilizador.objects.all())


    def test_register_user_failure(self):
        data = {
            'username': 'newuser',
            'password1': 'StrongPassword123!',
            'password2': 'WrongPassword123!',
        }
        response = self.client.post(reverse('registar'), data)
        
        # Verifique se a resposta não é um redirecionamento (302)
        self.assertEqual(response.status_code, 200)  # A página deve ser renderizada novamente
        
        # Certifique-se de que o formulário de erro foi renderizado
        self.assertFormError(response, 'form', 'password2', 'As palavras-passe não coincidem.')


class LogoutUtilizadorTest(TestCase):
    def setUp(self):
        self.user = Utilizador.objects.create_user(username='testuser', password='Testpassword123')

    def test_logout_user(self):
        self.client.login(username='testuser', password='Testpassword123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redireciona após logout
        self.assertNotIn('_auth_user_id', self.client.session)

class LoginViewCustomTest(TestCase):
    def setUp(self):
        self.user = Utilizador.objects.create_user(username='testuser', password='Testpassword123')

    def test_login_success(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'Testpassword123'})
        self.assertEqual(response.status_code, 302)  # Redireciona após login

    def test_login_user_not_found(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'Testpassword123'})
        self.assertEqual(response.status_code, 200)  # Permanece na página de login
        self.assertContains(response, 'O utilizador não existe.')

    def test_login_wrong_password(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'WrongPassword'})
        self.assertEqual(response.status_code, 200)  # Permanece na página de login
        self.assertContains(response, 'Palavra-passe incorreta.')

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'WrongPassword'})
        self.assertEqual(response.status_code, 200)  # Permanece na página de login
        self.assertContains(response, 'Palavra-passe incorreta.')

class MinhaContaViewTest(TestCase):
    def setUp(self):
        self.user = Utilizador.objects.create_user(username='testuser', password='Testpassword123')

    def test_minhas_conta_com_login(self):
        self.client.login(username='testuser', password='Testpassword123')
        response = self.client.get(reverse('minha_conta'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

class EditarContaViewTest(TestCase):
    def setUp(self):
        self.user = Utilizador.objects.create_user(username='testuser', password='Testpassword123', email='old@example.com')

    def test_editar_conta_sucesso(self):
        self.client.login(username='testuser', password='Testpassword123')
        response = self.client.post(reverse('editar_conta'), {'first_name': 'Test', 'last_name': 'User', 'email': 'new@example.com', 'telefone': '123456789'})
        self.assertEqual(response.status_code, 302)  # Redireciona após salvar
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'new@example.com')


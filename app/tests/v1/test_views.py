import unittest
import json
import app.api.v1.models import destroy
from app import create_app
from instance.config import app_config


class ApiTests(unittest.TestCase):
    def setUp(self):
        # destroy()
        self.app = create_app(config_name='testing')
        self.test_client = self.app.test_client()

        self.user_info = json.dumps({
            "firstname": "paul',
            "lastname": "mwangi",
            "othername": "kamau",
            "email": "paul@gmail.com,
            "phoneNumber": "0722000000",
            "username": "paul-mwangi",
            "isAdmin": "no",
        })

        self.meetup_info = json.dumps({
            "location": "Nairobi,Kenya",
            "images": "/images/setup",
            "topic": "Current trends React Js",
            "happeningOn": "14/01/2019",
            "Tags": []
        })

        self.question_info = json.dumps({
            "meetup": 1,
            "title": "Integrate React Js with google maps",
            "body": "How dow integrate React Js with google maps",
            "votes": 10
        })

        self.meetup_rsvp = json.dumps({
            "meetup": 1,
            "user": 2,
            "response": "I will attend"
        })

        signup_user = self.test_client.post("/api/v1/auth/signup",
                                            data=self.user_info,
                                            content_type='application/json')

        create_meetup =  self.test_client.post("/api/v1/meetups",
                                            data =self.meetup_info,
                                            content_type='application/json')

        create_question =  self.test_client.post("/api/v1/questions",
                                            data =self.question_info,
                                            content_type='application/json')  

        create_rsvp =  self.test_client.post("/api/v1/meetups/1/1",
                                            data =self.question_info,
                                            content_type='application/json')  

        self.context = self.app.app_context()
        self.context.push()

        def tearDown(self):
            destroy()
            return self.context.pop()     

        def test_user__signup(self):
            """Test User Signup"""
            user_info = json.dumps({
                 "firstname": "ezra',
                "lastname": "mugambi",
                "othername": "momina",
                "email": "ezramugambi@gmail.com,
                "phoneNumber": "0722000000",
                "username": "ezra-mugambi",
                "isAdmin": "no",
            })
            response = self.test_client.post("/api/v1/auth/signup",
                                            data=user_info,
                                            headers={
                                                'content-type': 'application/json'
                                            })
            self.assertEqual(response.status_code, 201) 

        def test_existing_username(self):
            user = json.dumps({
                "firstname": "ezra',
                "lastname": "mugambi",
                "othername": "momina",
                "email": "ezramugambi@gmail.com,
                "phoneNumber": "0722000000",
                "username": "ezra-mugambi",
                "isAdmin": "no"
            })

            response = self.test_client.post("/api/v1/auth/signup", data=user,
                                            headers={
                                                'content-type': 'application/json'})
            self.assertEqual(json.loads(response.data)['erro'], "Username 'ezra-mugambi' already taken")
            self.assertEqual(response.status_code, 409)  

        def test_create_meetup(self):
            """Test admin can create meetup record"""
            meetup = json.dumps({
                 "location": "Nairobi,Kenya",
                "images": "/images/setup",
                "topic": "Current trends React Js",
                "happeningOn": "14/01/2019",
                "Tags": []
            })
            response = self.test_client.post("/api/v1/auth/signup",
                                            data=meetup,
                                            headers={
                                                'content-type': 'application/json'
                                            })
            self.assertEqual(response.status_code, 201) 

        def test_create_question(self):
            """Test user  can post a question to a meetup"""
            question = json.dumps({
                "title": "Test React redux apps",
                "body": "How do one test react redux applications",
                "votes": 9
            })
            response = self.test_client.post("/api/v1/questions",
                                            data=question,
                                            headers={
                                                'content-type': 'application/json'
                                            })
            self.assertEqual(response.status_code, 201) 

        def test_create_meetup_rsvp(self):
            """Test user can create an  rsvp"""
            rsvp = json.dumps({
                "meetup": 1,
                "user": 2,
                "response": "I will attend"
            })
            response = self.test_client.post("/api/v1/questions",
                                            data=rsvp,
                                            headers={
                                                'content-type': 'application/json'
                                            })
            self.assertEqual(response.status_code, 201)  

        def test_upvote_question(self):
            """Test user can upvote a question"""
            response = self.test_client.patch("/api/v1/questions/1/upvote",
                                            headers={
                                                'content-type': 'application/json'
                                            })
            self.assertEqual(response.status_code, 200)   

        def test_downvote_question(self):
            """Test user can downvote a question"""
            response = self.test_client.patch("/api/v1/questions/1/downvote",
                                            headers={
                                                'content-type': 'application/json'
                                            })
            self.assertEqual(response.status_code, 200)           


        def test_user_get_all_meetups(self):
            response = self.test_client.get('/api/v1/meetups/upcoming', headers={
                'content-type': 'application/json'})
            self.assertEqual(response.status_code, 200)

        def test_user_get_single_meetup(self):
            response = self.test_client.get('/api/v1/meetups/1', headers={
                'content-type': 'application/json'})
            self.assertEqual(response.status_code, 200)                                                                                                                                                     


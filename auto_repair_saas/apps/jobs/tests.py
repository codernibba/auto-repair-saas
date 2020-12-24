from django.contrib.messages import get_messages
from django.urls import reverse
from faker import Faker

from auto_repair_saas.apps.contacts.tests import ContactFactory
from auto_repair_saas.apps.utils.factories import JobFactory
from auto_repair_saas.apps.utils.tests import BaseTestCase
from auto_repair_saas.apps.vehicles.tests import VehicleFactory

fake = Faker()


class JobsTestCase(BaseTestCase):
    def test_get_jobs_page(self):
        response = self.client.get(reverse('jobs'))
        self.assertEqual(response.status_code, 200)

    def test_post_new_job(self):
        client = ContactFactory()
        vehicle = VehicleFactory(owner=client)
        data = {
            'client': client.id,
            'vehicle': vehicle.id,
            'charged': fake.random_int()
        }
        response = self.client.post(reverse('jobs'), data)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertTrue(len(messages) == 1)
        self.assertEqual('Job created.', messages[0])

    def test_post_new_job_error(self):
        response = self.client.post(reverse('jobs'), {})
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertTrue(len(messages) == 1)
        self.assertEqual('Form is invalid.', messages[0])

    def test_update_job(self):
        job = JobFactory()
        data = {
            'client': job.client.id,
            'vehicle': job.vehicle.id,
            'charged': job.charged + 1
        }
        response = self.client.post(
            reverse('update-job', kwargs={'pk': job.id}), data
        )
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertTrue(len(messages) == 1)
        self.assertEqual('Job updated.', messages[0])

    def test_delete_job(self):
        job = JobFactory()
        response = self.client.post(
            reverse('delete-job', kwargs={'pk': job.id})
        )
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertTrue(len(messages) == 1)
        self.assertEqual('Job deleted.', messages[0])

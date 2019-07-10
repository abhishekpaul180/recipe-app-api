from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Store_link

from picUploads.serializers import Store_linkSerializer

STORE_LINK_URL = reverse('picUploads:store_link-list')


class PublicStore_linkApiTests(TestCase):
    """Test the publicly available store_link API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test login is required to access the endpoint"""
        res = self.client.get(STORE_LINK_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateStore_linkApiTests(TestCase):
    """Test the private store_link API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@afleh.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_store_link_list(self):
        """Test retrieving a list of store_link"""
        Store_link.objects.create(user=self.user,
                                  name="https://www.zappos.com/p/shan-the-week-end-racerback-dress-cover-up-onyx/product/9317750/color/19488")
        Store_link.objects.create(user=self.user,
                                  name="https://www.myntra.com/tshirts/us-polo-assn-denim-co/us-polo-assn-denim-co-men-black-printed-round-neck-t-shirt/8589327/buy")

        res = self.client.get(STORE_LINK_URL)

        store_link = Store_link.objects.all().order_by('-name')
        serializer = Store_linkSerializer(store_link, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_status_link_limited_to_user(self):
        """Test that only store_link for the authenticated user are returned"""
        user2 = get_user_model().objects.create_user(
            'test@google.com',
            'testpass'
        )
        Store_link.objects.create(user=user2,
                                  name='https://www.zappos.com/p/shan-the-week-end-racerback-dress-cover-up-onyx/product/9317750/color/19488')
        store_link = Store_link.objects.create(user=self.user,
                                               name='https://www.myntra.com/tshirts/us-polo-assn-denim-co/us-polo-assn-denim-co-men-black-printed-round-neck-t-shirt/8589327/buy')

        res = self.client.get(STORE_LINK_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], store_link.name)

    def test_create_store_link_successful(self):
        """Test create a new store_link"""
        payload = {'name': 'www.zappos.com'}
        self.client.post(STORE_LINK_URL, payload)

        exists = Store_link.objects.filter(
            user=self.user,
            name=payload['name'],
        ).exists()
        self.assertTrue(exists)

    def test_create_store_link_invalid(self):
        """Test creating invalid store link fails"""
        payload = {'name': ''}
        res = self.client.post(STORE_LINK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)



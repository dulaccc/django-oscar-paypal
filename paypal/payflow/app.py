from django.conf.urls.defaults import patterns, url
from django.contrib.admin.views.decorators import staff_member_required

from oscar.core.application import Application
from oscar.apps.dashboard.nav import register, Node

from paypal.payflow import views

node = Node('PayPal', 'paypal-payflow-list')
register(node, 100)


class PayFlowDashboardApplication(Application):
    name = None
    list_view = views.TransactionListView
    detail_view = views.TransactionDetailView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^transactions/$', self.list_view.as_view(),
                name='paypal-payflow-list'),
            url(r'^transactions/(?P<pk>\d+)/$', self.detail_view.as_view(),
                name='paypal-payflow-detail'),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = PayFlowDashboardApplication()

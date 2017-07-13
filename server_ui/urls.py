# -*- coding: utf-8 -*-
from django.conf.urls import *

from signbook.views import IndexView, MerkleView, MerkleResultView
from views import *

urlpatterns = patterns('',
  (r'^home$', home),
  (r'^$', IndexView.as_view()),
  (r'^about$', about),
  (r'^docs$', docs),
  (r'^faq$', faq),
  (r'^privacy$', privacy),
  (r'^merkle$', MerkleView.as_view()),
  (r'^merkle_result$', MerkleResultView.as_view()),
)

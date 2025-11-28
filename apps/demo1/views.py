from django.views.generic import TemplateView
from typing import Dict, Any


class IndexView(TemplateView):
    """Main dashboard view for demo1 with sidebar layout."""

    template_name = 'demo1/index.html'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # Add your hardcoded dashboard data here
        context.update({
            'page_title': 'Dashboard',
            'page_description': 'Central Hub for Personal Customization',
            # Add stats, activities, projects data...
        })

        return context
# Ecommerce Automation Testing

### Project Structure

```text
ecommerce_automation/
│
├── features/
│   ├── cart_add.feature
│   ├── cart_remove.feature
│   ├── categories.feature
│   ├── invalid_login.feature
│   ├── login.feature
│   ├── navigation_home.feature
│   ├── order_confirmation.feature
│   ├── place_order.feature
│   ├── product_details.feature
│   ├── signup_duplicate.feature
│   ├── signup.feature
│   └── top_navigation_bar.feature
│
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── duplicate_signup.py
│   ├── home_page.py
│   ├── invalid_login.py
│   ├── login_page.py
│   ├── navigation_home.py
│   ├── order_page.py
│   ├── product_page.py
│   └── signup_page.py
│
├── reports/
│   └── report.html
│
├── tests/
│   ├── test_cart.py
│   ├── test_categories.py
│   ├── test_login.py
│   ├── test_navigation.py
│   ├── test_negative_auth.py
│   ├── test_order.py
│   ├── test_product_detail.py
│   ├── test_signup.py
│   └── test_top_navigation.py
│
├── utils/
│   └── drivers.py
│
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore
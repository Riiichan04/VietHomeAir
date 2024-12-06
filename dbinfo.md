# File này dùng để lưu thông tin database của web

#### Tài khoản
- accounts:
  - id*
  - username
  - password
  - email
  - fullname
  - gender
  - role

##### Dành cho chủ bnb:
- owners:
  - id*
  - rating
  - count_rating

- bnb_owners:
    - bnb_id*
    - account_id*

#### Trong các bảng bnb th id = bnb_id 
- bnb_details:
  - id*
  - name
  - description
  - address
  - price
  - capacity (Chứa được bao nhiêu người)
  - count_viewed

- bnb_services: (Tiện ích của bnb)
  - id*
  - name*

- bnb_images:
  - id*
  - image_url*

- bnb_comments: (Đánh giá của bnb)
    - comment_id*
    - bnb_id*
    - username
    - comment
    - rating
    - type

- bnb_rules: (Nội quy của bnb)
  - id*
  - name*
  - description

#### Danh mục

- categories
  - id*
  - name

- category_details
  - id*
  - bnb_id*

#### Yêu thích
- wishlists: (Phần yêu thích)
  - account_id*
  - bnb_id*
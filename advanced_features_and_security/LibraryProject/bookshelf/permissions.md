# Advanced Features and Security – Permissions and Groups

This project demonstrates how to manage **permissions** and **groups** in Django using a custom user model and the `Book` model.

---

## Step 4: Test Permissions

### Testing Approach
1. **Create Test Users**
   - Add 3 test users via Django Admin (`/admin`).

2. **Assign Users to Groups**
   - Go to **Admin → Groups** and create the following groups:
     - **Viewers** → assign `can_view`
     - **Editors** → assign `can_view`, `can_create`, `can_edit`
     - **Admins** → assign `can_view`, `can_create`, `can_edit`, `can_delete`

   - Assign each test user to one of these groups.

3. **Log In and Test Access**
   - **Viewer User**:
     - ✅ Can access `/books/` (requires `can_view`)
     - ❌ Cannot access `/books/add/`, `/books/<id>/edit/`, `/books/<id>/delete/`

   - **Editor User**:
     - ✅ Can access `/books/` (requires `can_view`)
     - ✅ Can add `/books/add/` (requires `can_create`)
     - ✅ Can edit `/books/<id>/edit/` (requires `can_edit`)
     - ❌ Cannot delete `/books/<id>/delete/` (missing `can_delete`)

   - **Admin User**:
     - ✅ Can access all views (`can_view`, `can_create`, `can_edit`, `can_delete`)

---

## Step 5: Document the Setup

### Custom Permissions
The `Book` model defines four custom permissions:
- `can_view` → Allows viewing the list of books.
- `can_create` → Allows creating new books.
- `can_edit` → Allows editing existing books.
- `can_delete` → Allows deleting books.

### Groups and Roles
- **Viewers** → Assigned `can_view`
- **Editors** → Assigned `can_view`, `can_create`, `can_edit`
- **Admins** → Assigned `can_view`, `can_create`, `can_edit`, `can_delete`

### Views and Permissions Mapping
- `/books/` → Requires `can_view`
- `/books/add/` → Requires `can_create`
- `/books/<id>/edit/` → Requires `can_edit`
- `/books/<id>/delete/` → Requires `can_delete`

---

## Notes
- Permissions are enforced with `@permission_required` decorators in `views.py`.
- Unauthorized users will see a **403 Forbidden** error if they try to access restricted views.
- This setup ensures a role-based access control system with clear separation of responsibilities.

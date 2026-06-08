def add_groups(response, user, backend, *args, **kwargs):
    from netbox.authentication import Group

    groups = response.get("groups", [])

    for group_name in groups:
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)


def remove_groups(response, user, backend, *args, **kwargs):
    from netbox.authentication import Group

    groups = response.get("groups")
    if groups is None:
        user.groups.clear()
        return

    user_groups = [item.name for item in user.groups.all()]
    delete_groups = set(user_groups) - set(groups)

    for delete_group in delete_groups:
        group = Group.objects.get(name=delete_group)
        user.groups.remove(group)


def set_roles(response, user, backend, *args, **kwargs):
    groups = response.get("groups", [])

    user.is_superuser = "AdminsIT" in groups
    user.is_staff = "staff" in groups
    user.save()

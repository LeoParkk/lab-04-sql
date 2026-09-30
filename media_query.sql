SELECT u.name, u.location, p.post_id, p.title
FROM users u
JOIN posts p ON u.user_id = p.user_id
WHERE u.location = 'LA';

from modules import AutoRequest

request = AutoRequest(
    method='POST',
    url='http://localhost:5000/post.php',
    loop=3,
    data={
        'username': 'Sulhan',
        'password': '123'
    }
)

request.run()

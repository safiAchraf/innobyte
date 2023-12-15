
### Database Schema : 
You can access it via [DrawSQL](https://drawsql.app/teams/safi-2/diagrams/innobyte)



## Tech Used

- **Back-End**: Django, Django REST framework
- **Database**: for now just SQlite 3 , in production we could use PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)

## End Points

- **api/register/** :
  let the user sign up , add him to the selected group of users . returns a response of the **{access token & the refresh token}**
- **api/signin/** :
  let the user signin , . returns a response of the **{access token & the refresh token}**

- **api/token/refresh** :
  returns a new access token by submitting the refresh token if its not expired .

- **api/getUser/** :
  returns the info of the user making the request

- **api/reservation/** :
    GET : returns the list of all the reservation if teh user making the request is Admin
    POST : checks first if the targted room is available , then create a reservation for that .


- **api/tasks/** :

  GET : return the list of tasks ;
  POST : let the superUser create new Tasks.
  PUT : update the status of completing of the task

- **api/staffuser/ **
  let the superUser to create a staff accounts for his workers.

- **api/rooms/ **
  Offers CRUD ( create , read , update , delete ) operations for hotel rooms.

  
  

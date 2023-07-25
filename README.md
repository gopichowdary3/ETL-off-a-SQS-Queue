# ETL-off-a-SQS-Queue
I have used AWS EC2 Instance for this Test (Linux Operating System)
Step 1: 
Install Docker-Compose using -  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
Then change its mode by using - sudo chmod +x /usr/local/bin/docker-compose
Check its version using : docker-compose --version

Step 2:
Now build the docker-compose.yml file using : docker-compose up -d

Step 3:(to install pip manager use the following commands)
sudo yum update -y

Step 4: 
Now install boto3 using :  pip3 install boto3 psycopg2-binary

Step 5: 
[ec2-user@ip-172-31-81-23 ~]$ aws configure
AWS Access Key ID [None]: xxxxxxxxxxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Default region name [your_region_name]: us-east-1
Default output format [None]: json

Step 6:
[ec2-user@ip-172-31-81-23 ~]$ python3 pythoncodeforETL.py

Step7:
[ec2-user@ip-172-31-81-23 ~]$ docker exec -it e6560cac0cee psql -U postgres
psql (10.21 (Debian 10.21-1.pgdg90+1))
postgres=# SELECT * FROM user_logins;


OUPUT:


                user_id                | device_type |            masked_ip             |         masked_device_id         | locale | app_version | create_date
--------------------------------------+-------------+----------------------------------+----------------------------------+--------+-------------+-------------
 424cdd21-063a-43a7-b91b-7ca1a833afae | android     | a56e7589b4b780605f7c614d13df6696 | 1237b6b78f6293ce2714d52b209eb3b4 | RU     | 2.3.0       |
 c0173198-76a8-4e67-bfc2-74eaa3bbff57 | ios         | 177bc093bf2ec84c9c4132428c362658 | a1085149d8942646625fcc3d0675a841 | PH     | 0.2.6       |
 66e0635b-ce36-4ec7-aa9e-8a8fca9b83d4 | ios         | 612b8dc672829f489c39e3a42bb58c9b | dbda58efa08b5c3d10ededfb4cb7327b |        | 2.2.1       |
 181452ad-20c3-4e93-86ad-1934c9248903 | android     | d3c1f3bb97c784786e40a17ef3cd6840 | 24d329f0137e0deea06a25d9a17e2c11 | ID     | 0.96        |
 60b9441c-e39d-406f-bba0-c7ff0e0ee07f | android     | 90953df5cd9402cd0bffec27608623bc | 077c18a43906fc44531de05a0a5e521e | FR     | 0.4.6       |
 5082b1ae-6523-4e3b-a1d8-9750b4407ee8 | android     | 065c73a32433c048bc7008c51c5febff | 33ee0add94833616f8b8fe8a95fd0d25 |        | 3.7         |
 5bc74293-3ca1-4f34-bb89-523887d0cc2f | ios         | 0792c36631f5bee042b0e742696990b1 | 6e71d4f238823c98262dd16d62d580f0 | PT     | 2.2.8       |
 92d8ceec-2e12-49f3-81bd-518fe66971ec | android     | 496bb11ea4e9485ec45102c4a2c581a5 | 6691be7b9016ab1ead28ef947aabbc38 | BR     | 0.5.5       |
 05e153b1-4fa1-474c-bd7e-9f74d1c495e7 | android     | 0c9ececf24a836c351f390351741a130 | 6704aedc4b6aa26bde4e8cc048d6c828 |        | 0.5.0       |
 325c0f3d-da25-45ff-aff4-81816db069bc | android     | 22b11ec443e8b693edcb720e41681fd2 | 0225079ca5b293128b6517011e94a33c | RU     | 0.60        |
 692bef80-12db-4f19-b142-60d7cf450eda | ios         | 18490b71b4c18c5b61dcd418a6346d4c | 68febf4426249a06c65170cc65a638d2 |        | 6.4.8       |
 9135d7bf-5992-4cfd-84bb-52b52030a748 | android     | a6ead9142fa10c7b2bcc0d5b1b0a5c23 | b7bbe7500fd8c6754f2982f238fc62c2 |        | 0.16        |
 6c72164e-1b7a-446a-906d-fedb45d8f718 | ios         | 69458e3cd4279208fc196f31ac6d9687 | 4255d990bbf6b2fc9a61003bf6421638 | KE     | 2.0.8       |
 2d839c07-94fd-4dd8-b535-a21ac271fea3 | ios         | 16bb8c9c4f1e8127be85577c47005b49 | d96a83e98ad210b95e2e87fc314e4832 |        | 7.31        |
 271bd27b-19e9-46c9-a5a4-7c2bb5e35cb0 | ios         | 5dc08aebdb5e66af2a00d58998906c9f | 701433efc0aec4d75171a337114b43ee | PE     | 7.87        |
 5e802e77-427d-4618-b437-ad4fb1461c0d | ios         | 1f7ea9a3c03193d328ef14db943407d3 | 301fddaa65feed89e792137444a8d336 | ID     | 6.80        |
 901905c7-a1ef-47bf-b28b-8f8d3f8df807 | ios         | 269d8234d363c258162dd78e62607102 | acc95db0b38a3551a1abb099f3943e61 | KR     | 5.56        |
 b018771c-cef7-42af-b595-83bf78cea441 | android     | 691e8af6a931a798a93a4905278ca035 | 6f0fe4dd5078295fa6faab351f0572d8 | KR     | 1.1         |
 74847efb-c793-4336-b7be-79b46793d05b | android     | 091213e1a3751e3554ea78244a497e0b | ed20fb4ff0ce38b1f069a676aca5b4b2 |        | 5.4.8       |
 ed5d5d23-590e-4c7c-ace0-dc8204630b14 | ios         | 18b2baeaf0e565d65bda29383b0fe8ce | 57b2ee5aeece14eb1569a1e86eb538a5 | ID     | 3.0         |
 d34e2144-9952-466e-bfbd-e8777f841cc8 | android     | 6741b94e79cba26a0112c136709cf932 | f4bd6212c88ae8e67786360b4cc6e250 |        | 2.2.9       |
 2fa29cb4-c70d-4f13-977c-fb8a7fdb3641 | ios         | 12501914c29123d88cbb4288f2bcd565 | 9016264b138828b0525e729f00510e7b |        | 5.60        |
 e1718797-aee8-42ec-bce7-550342cb2653 | android     | 52f9ea9b3ef161623cda94b1289c49aa | 35d9931ceee19cbcfbad82a1b0f3f5e9 | CN     | 6.02        |
 fd75e212-7bc4-4bc5-a307-34c7a57b9ecc | android     | 4a092ea654521d75103b85c7266fa8c5 | 3fec387d4c008c9b761108e9508ea5eb | RU     | 0.32        |
 1cd051c7-3211-48ea-b3bf-321fafa741e1 | ios         | 489e95cff3e29c4187cfa0397b68ce48 | 1dcf4ff5a62b54486e27a1e2953a3899 | MT     | 0.65        |
 780bf10e-d397-4e02-b7b4-85e5dc096c7b | android     | 1c2d052e7bd4d257bcc8ffe9551a0934 | a9025b3515add4474b50650644f2eb67 | GR     | 1.8.0       |
 33350db1-0a80-4a75-9909-d143386405f7 | android     | c81da89b5bf24552d7ff410c11a8fdfe | 187f5d853be6345340b309bda725a692 |        | 5.6.7       |
 806338fd-8c23-4554-a703-bcd1f1549286 | android     | 833c76ea4cd28c59d658af27aae36598 | 247cba0e0f6289e6eb84c61b6388ff86 |        | 2.6         |
 c816a7e6-a7f4-4cf3-ae12-d3c927fbeac5 | ios         | da30a87508589c17b5e02a71798e454c | 1c2dd3f8645c25b4df9851cfe8acb494 | PH     | 9.10        |
 f7f0ee55-997a-4e87-946a-68d0dfb35d12 | ios         | 4f866f61e38a1d044f871a6a79b890e8 | 8acc6ced2a324e91a8c98c368ef3de20 |        | 4.19        |
 
 





Blockers: 
Error: 
File "pythoncodeforETL.py", line 88, in <module>
    fetch_message_from_queue()
  File "pythoncodeforETL.py", line 42, in fetch_message_from_queue
    write_to_postgres(msg_body)
  File "pythoncodeforETL.py", line 77, in write_to_postgres
    cur.executemany(sql, values)
psycopg2.errors.InvalidTextRepresentation: invalid input syntax for integer: "2.3.0"
LINE 1: ...f6696', '1237b6b78f6293ce2714d52b209eb3b4', 'RU', '2.3.0', N...

The error I encountered came from trying to insert a string where PostgreSQL expects an integer. 
In our SQL insert statement, one of your variables is being inserted as a string when it's meant to be an integer. 
The specific error was caused by trying to insert the string "2.3.0" into an integer field. 
From our logs, it appears that "2.3.0" corresponds to app_version.
It looks like app_version is a string representing version numbers and not an integer.

If app_version is indeed supposed to be a string, change the datatype of this field in your database to text or varchar.
To alter the datatype of a column in a PostgreSQL table, you can use the ALTER TABLE command. 

For this go to psql service using : docker exec -it <container_id_or_name> psql -U postgres
Now execute the following command using psql : ALTER TABLE user_logins ALTER COLUMN app_version TYPE VARCHAR;


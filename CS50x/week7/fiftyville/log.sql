-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Access to the information from crime_scene_reports:
SELECT * FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND street = "Humphrey Street";

-- Access to the interviews of three witnesses, take a look to the interviews which call "bakery" inside (161, 162, 163)
SELECT * FROM interviews
WHERE day = 28 AND month = 7;

-- Access to the atm_transactions on 28/7/2021, Leggett Street and using withdraw
SELECT * FROM atm_transactions
WHERE day = 28 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";

-- Access to the phone_calls on 28/7/2021, duration < 60s
SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60;

-- Access to airports to get the id of Fiftyville (id = 8)
SELECT * FROM airports;

-- Access to flights to get des_id on day 29, ori_id = 8
-- Note: the thief will take the earliest flight
SELECT * FROM flights WHERE origin_airport_id = 8 AND day = 29 ORDER BY hour ASC;
-- According to above command, we will take the first flight in the table
-- Then we get the flight id = 36

-- Using under command to get the passport_number in flight_id 36
SELECT * FROM passengers WHERE flight_id = 36;


-- Using under command to get id and name; (we get 5 people)
SELECT * FROM people
WHERE passport_number
IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number
IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60);

-- Using under command to get the account_number in bank_accounts of 5 people above
SELECT * FROM bank_accounts
WHERE person_id
IN (SELECT id FROM people
WHERE passport_number
IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number
IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60));
-- After using above command, we will get information of 3 people
-- then we will compare it with the account_number which we have got from atm_transactios

SELECT * FROM atm_transactions
WHERE day = 28
AND account_number
IN (SELECT account_number FROM bank_accounts
WHERE person_id
IN (SELECT id FROM people
WHERE passport_number
IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number
IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60)));

-- NOTE: The thief get into a car about 10mins after the theft
-- So we will check the license_plate
SELECT * FROM bakery_security_logs
WHERE day = 28 AND month = 7 AND hour = 10 AND minute <= 25 AND activity = "exit"
AND license_plate
IN (SELECT license_plate FROM people
WHERE passport_number
IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number
IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60));

-- after checking all the information, we get these important infomation
-- LICENSE_PLATE: 94KL13X; G412CB7; 0NTHK55
-- ACCOUNT_NUMBER & PERSON_ID: 49610011 & 686048, 28296815 & 395717, 76054385 & 449774

-- the last step, we need to find out who is the thief
SELECT * FROM people
WHERE license_plate IN ("94KL13X", "G412CB7", "0NTHK55")
AND id IN ("686048", "395717", "449774");

-- after using the above command, the thief is Bruce
-- Bruce: +id: 686048; +phone_number: (367) 555-5533; +passport_number: 5773159633; +license_plate: 94KL13X

-- find the city where Bruce escape to
--flight id = 36, ori_id = 8 (Fiftyville), des_id = 4 (New York City)

-- find the receiver: +number: (375) 555-8161
SELECT * FROM people WHERE phone_number = "(375) 555-8161";



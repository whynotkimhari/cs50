document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form .btn').addEventListener('click', send_email);
  // By default, load the inbox
  load_mailbox('inbox');
});

function send_email(e) {
  const recipients = document.querySelector("#compose-recipients");
  const subject = document.querySelector("#compose-subject");
  const body = document.querySelector("#compose-body");

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: Array.from(new Set(recipients.value.split(','))).toString(),
      subject: subject.value,
      body: body.value
    })
  })
  .then(rs => rs.json())
  .then(() => load_mailbox('sent'));
  e.preventDefault();
}

function compose_email() {
  
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function mark_as_read(id) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  })
}

function mark_as_unread(id) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: false
    })
  })
}

function reply(id) {
  console.log("mail " + id + " reply")
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  fetch(`/emails/${id}`)
  .then(rs => rs.json())
  .then(data => {
    console.log(data)
    document.querySelector('#compose-recipients').value = `${data.sender}`;
    document.querySelector('#compose-subject').value = data.subject.startsWith('Re: ') ? data.subject : `Re: ${data.subject}`;
    document.querySelector('#compose-body').value = `\n\n--------------------------------\nOn ${data.timestamp} ${data.sender} wrote:\n\n${data.body}`;
    document.querySelector('#compose-body').setAttribute('autofocus', 'autofocus');
    document.querySelector('#compose-body').setSelectionRange(0, 0);
    document.querySelector('#compose-body').focus();
  })
}

function set_archive(id) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: true
    })
  })
  .then(() => load_mailbox('inbox'))
}

function set_unarchive(id) {
  console.log(id)
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: false
    })
  })
  .then(() => load_mailbox('inbox'))
}

function open_mail(id, mailbox_type) {
  mark_as_read(id);
  fetch(`/emails/${id}`)
  .then(rs => rs.json())
  .then(data => {
    // console.log(data)
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    if(mailbox_type === 'inbox') {
      console.log(data.body)
      document.querySelector('#emails-view').innerHTML = `
        <div>
          <strong>From</strong>: ${data.sender}<br/>
          <strong>To</strong>: ${data.recipients.toString()}<br/>
          <strong>Subject</strong>: ${data.subject}<br/>
          <strong>Timestamp</strong>: ${data.timestamp}<br/>
          <button onclick="reply(${id})">Reply</button>
          <button onclick="set_archive(${id})">Archive</button>
          <hr>
          <pre style="font-size: 16px !important;">${data.body}</pre>
        </div>
      `
    }
    else if (mailbox_type === 'sent') {
      document.querySelector('#emails-view').innerHTML = `
        <div>
          <strong>From</strong>: ${data.sender}<br/>
          <strong>To</strong>: ${data.recipients.toString()}<br/>
          <strong>Subject</strong>: ${data.subject}<br/>
          <strong>Timestamp</strong>: ${data.timestamp}<br/>
          <button onclick="reply(${id})">Reply</button>
          <hr>
          <pre>${data.body}</pre>
        </div>
      `
    }
    else if (mailbox_type === 'archive') {
      document.querySelector('#emails-view').innerHTML = `
        <div>
          <strong>From</strong>: ${data.sender}<br/>
          <strong>To</strong>: ${data.recipients.toString()}<br/>
          <strong>Subject</strong>: ${data.subject}<br/>
          <strong>Timestamp</strong>: ${data.timestamp}<br/>
          <button onclick="reply(${id})">Reply</button>
          <button onclick="set_unarchive(${id})">Un-Archived</button>
          <hr>
          <pre>${data.body}</pre>
        </div>
      `
    }
    // console.log(data);
  })
}

function load_mailbox(mailbox) {
  // console.log(mailbox);
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // console.log(emails, mailbox);
    if(mailbox === 'inbox') {
      emails.forEach(email => {
        let html = `
          <div class="email-section" onclick="open_mail(${email.id},'inbox')" style="background: ${email.read ? 'gainsboro' : 'white'}">
            <div class="row">
                <div class="sender">To: <strong>${email.sender}</strong></div>
                <div class="header">${email.subject}</div>
              </div>   
              <div class="timestamp"><sub>${email.timestamp}</sub></div>
          </div>
        `;
        document.querySelector('#emails-view').innerHTML += html;
      })
    }

    else if(mailbox === 'sent') {
      emails.forEach(email => {
        email.recipients.forEach(recipient => {
          let html = `
            <div class="email-section" onclick="open_mail(${email.id},'sent')" style="background: ${email.read ? 'gainsboro' : 'white'}">
              <div class="row">
                <div class="recipient">To: <strong>${recipient}</strong></div>
                <div class="header">${email.subject}</div>
              </div>   
              <div class="timestamp"><sub>${email.timestamp}</sub></div>
            </div>
          `;
          document.querySelector('#emails-view').innerHTML += html;
        })
      })
    }

    else if(mailbox === 'archive') {
      emails.forEach(email => {
        let html = `
          <div class="email-section" onclick="open_mail(${email.id},'archive')" style="background: ${email.read ? 'gainsboro' : 'white'}">
            <div class="row">
                <div class="sender">To: <strong>${email.sender}</strong></div>
                <div class="header">${email.subject}</div>
              </div>   
              <div class="timestamp"><sub>${email.timestamp}</sub></div>
          </div>
        `;
        document.querySelector('#emails-view').innerHTML += html;
      })
    }
    
    // console.log(emails)
  });
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}
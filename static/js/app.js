// let contacts = [];

// let contactForm = document.getElementById("new-contact-form");


// function addContact(event) {
//   event.preventDefault();
//   let form = event.target;

//   let newContact = {
//     id: generateId(),
//     name: form.contactName.value,
//     phone: form.contactPhone.value,
//     emergency: form.emergencyContact.checked
//   };

//   let existingContact = contacts.find(
//     contact => contact.name == form.contactName.value
//   ); 
//   if (!existingContact) {
//     contacts.push(newContact);
//     saveContacts();
//     form.reset();
//   }
//   document.getElementById("new-contact-form").classList.add("hidden");
//   document.getElementById("contactToggle").classList.remove("hidden");
// }


// function saveContacts() {
//   window.localStorage.setItem("contacts", JSON.stringify(contacts));
//   drawContacts();
// }


// function loadContacts() {
//   let contactsData = JSON.parse(window.localStorage.getItem("contacts"));
//   if (contactsData) {
//     contacts = contactsData;
//   }
// }

// // List View
// function drawContacts() {
//   let template = "";

//   contacts.forEach(contact => {
    
//     template += `
//       <div class="card mt-1 mb-1 ${
//         contact.emergency ? "emergency-contact" : ""
//       }"> 
//         <h3 class="mt-1 mb-1"><a href="#">${contact.name}</a></h3>
//         <div class="d-flex space-between">
//           <p>
//             <i class="fa fa-fw fa-phone"></i>
//             <span>${contact.phone}</span>
//           </p>
//           <i class="action fa fa-trash text-danger" onclick="removeContact('${
//             contact.id
//           }')"></i>
//         </div>
//       </div>
//     `;
//   });

//   document.getElementById("contact-list").innerHTML = template;
// }

// // Delete View
// function removeContact(contactId) {
//   let removeContactIndex = contacts.findIndex(
//     contact => contact.id === contactId
//   );
//   contacts.splice(removeContactIndex, 1);
//   saveContacts();
// }

// // TODO This will link to create view
// function toggleAddContactForm() {
//   if (!contactForm.classList.contains("hidden")) {
//     contactForm.classList.add("hidden");
//     document.getElementById("contactToggle").classList.remove("hidden");
//   } else {
//     contactForm.classList.remove("hidden");
//     document.getElementById("contactToggle").classList.add("hidden");
//   }
// }


// // Model
// function generateId() {
//   return (
//     Math.floor(Math.random() * 10000000) +
//     "_" +
//     Math.floor(Math.random() * 10000000)
//   );
// }

// // Views
// loadContacts();
// drawContacts();
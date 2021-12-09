$(document).ready(function () {
    if ($(window).width() > 991){
    $('.navbar-light .d-menu').hover(function () {
            $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
        }, function () {
            $(this).find('.sm-menu').first().stop(true, true).delay(120).slideUp(100);
        });
        }
    });

function open_modal_signin()
{
	document.getElementById("Modal").style.display = "block";
	document.getElementById("ModalTitle").innerHTML = `Authorization`;
	document.getElementById("ModalBody").innerHTML = `

    <form method="POST" action="lk/">
        <div class="form__group field" style="width:50%; margin-left:25%;">
            <input type="input" class="form__field" placeholder="email" id="email" required />
            <label for="name" class="form__label" align="center">Email</label>
        </div>
        <br><br>
        <div class="form__group field" style="width:50%; margin-left:25%;">
            <input type="input" class="form__field" placeholder="Password"  id='password' required />
            <label for="phone" class="form__label" align="center">Password</label>
        </div>
    
        <button class="registration" onclick="open_modal_registration()">Registration</button>
        <button class="enter" type="commit">Enter</button><br><br><br><br>
         
        <a type="button" href="recovery/" class="restore">Forgot pass?</a>
     
    </form>
`;

        // document.getElementById("ModalButtons").innerHTML = `
        //     <button class="registration" onclick="open_modal_registration()">Registration</button>
        //     <button class="enter" onclick="enterAccount()">Enter</button><br><br><br><br>
        //
        //     <a type="button" href="recovery/" class="restore">Forgot pass?</a>`;
}
function enterAccount(){
    console.log("!")
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
     $.ajax({
         url: "/api/enter_account/",
         method: "POST",
         data: {
             csrfmiddlewaretoken : csrf_token,
             form : document.getElementById("sign_in_form")
         },
         success: function (data) {

             console.log(data)
         },
         error(){
             console.log("error");
         }
     })
}

$("#sign_in_form").submit(function (){
    event.preventDefault();
    $.ajax({
        data: $(this).serialize(),
        type: $(this).attr('method'),
        url: "/api/enter_account/",

        success: function (response){
            let user_id = response.id;
            location.href =`/lk/${user_id}`;
        },
        error: function (response){
            console.log(response);
        }
    });
    return false;
})

$("#sign_up_form").submit(function (){
    event.preventDefault();
    $.ajax({
        data: $(this).serialize(),
        type: $(this).attr('method'),
        url: "/api/users/",

        success: function (response){
            console.log(response);
            //let user_id = response.id;
            //location.href =`/lk/${user_id}`;
        },
        error: function (response){
            console.log(response);
        }
    });
    return false;
})

            
function open_modal_registration()
{
	document.getElementById("Modal").style.display = "block";
	document.getElementById("ModalTitle").innerHTML = `<h3 align="center">Registration</h3>`;
	document.getElementById("ModalBody").innerHTML = `
    <div class="form_wrapper">
        <div class="form_container">
          <div class="title_container">
          </div>
          <div class="row clearfix">
            <div class="message">
                <div class="input_field"> <span><i aria-hidden="true" class="fa fa-envelope"></i></span>
                  <input type="email" name="email" placeholder="Email" id="email" />
                </div>
                <div class="input_field"> <span><i aria-hidden="true" class="fa fa-lock"></i></span>
                  <input type="password" name="password" placeholder="Password" id="password"/>
                </div>
                <div class="input_field"> <span><i class="fa fa-building"></i></span>
                    <input type="text" name="company" placeholder="Company" id="company"/>
                  </div>
                  <div class="input_field select_option">
                    <select id="country">
                      <option>Select a country</option>
                      <option>Russia</option>
                      <option>Italia</option>
                      <option>Germany</option>
                    </select>
                    <div class="select_arrow"></div>
                  </div>
                  <div class="input_field"> <span><i class="fa fa-map" aria-hidden="true"></i></span>
                    <input type="text" name="address" placeholder="Address" id="address"/>
                  </div>
                <div class="row clearfix">
                  <div class="col_half">
                    <div class="input_field">
                      <input type="number" name="postalcode" maxlength="6" id="postal_code"  placeholder="Zip code" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"> 
                      <input type="text" name="city" id="city" placeholder="City" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"> <span><i class="fa fa-phone"></i></span>
                      <input type="number" name="telephone" id="telephone" placeholder="Telephone" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"><span><i class="fa fa-desktop" aria-hidden="true"></i></span>
                      <input type="text" name="website" id="website" placeholder="Website" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"> <span><i aria-hidden="true" class="fa fa-user"></i></span>
                      <input type="text" name="firstname" id="first_name" placeholder="First Name" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"> <span><i aria-hidden="true" class="fa fa-user"></i></span>
                      <input type="text" name="lastname" id="last_name" placeholder="Last Name" />
                    </div>
                  </div>
                </div>
                <div class="input_field"> <span><i class="fa fa-hashtag" aria-hidden="true"></i></span>
                    <input type="text" name="position" id="post" placeholder="Position in the company" />
                  </div>
                  <div class="input_field select_option">
                    <select id="currency">
                      <option>Currency</option>
                      <option>EUR</option>
                      <option>USD</option>
                      <option>RUB</option>
                    </select>
                    <div class="select_arrow"></div>
                  </div>
                  <div class="input_field"> <span><i class="fa fa-industry" aria-hidden="true"></i></span>
                    <input type="text" name="industry" id="industry" placeholder="Industry in which your company is working" />
                  </div>
                  
                  <button class="main_reg" onclick="registration()">Registration</button>
            </div>
          </div>
        </div>`;

 
        document.getElementById("ModalButtons").innerHTML = ``;


}

function CloseModal()
 {
   document.getElementById("Modal").style.display = "none";
 }

//  function restore(){
//      prompt("Забыли пароль?");
//  }

 function hash(s){
  let res = s.split("").reduce(function(a,b){a=((a<<5)-a)+b.charCodeAt(0);return a&a},0);
  console.log(res);
  return res
}

 function registration() {
     csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
     $.ajax({
         url: "/api/users/",
         method: "POST",
         data: {
             csrfmiddlewaretoken : csrf_token,
             email : document.getElementById("email").value,
             password : document.getElementById("password").value,
             company : document.getElementById("company").value,
             country : document.getElementById("country").value,
             address : document.getElementById("address").value,
             postal_code : document.getElementById("postal_code").value,
             city : document.getElementById("city").value,
             phone_1 : document.getElementById("telephone").value,
             website : document.getElementById("website".value),
             first_name : document.getElementById("first_name").value,
             last_name : document.getElementById("last_name").value,
             post : document.getElementById("post").value,
             currency : document.getElementById("currency").value,
             industry : document.getElementById("industry").value,
             token : hash(document.getElementById("email").value)
         },
         success: function (data) {
             console.log(data)
         },
         error(){
             console.log("error");
         }
     })
 }


 function requestUser(){

 }
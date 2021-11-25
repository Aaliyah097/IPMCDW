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
    <div class="form__group field" style="width:50%; margin-left:25%;">
        <input type="input" class="form__field" placeholder="email" required />
        <label for="name" class="form__label" align="center">Email</label>
    </div>
    <br><br>
    <div class="form__group field" style="width:50%; margin-left:25%;">
        <input type="input" class="form__field" placeholder="Password"  id='password' required />
        <label for="phone" class="form__label" align="center">Password</label>
    </div>`;
	document.getElementById("ModalButtons").innerHTML = `
		<button class="registration" onclick="open_modal_registration()">Registration</button>
		<button class="enter" onclick="Enter()">Enter</button><br><br><br><br>
       
        <a type="button" href="recovery/" class="restore">Forgot pass?</a>
        
	`;
}


            
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
              <form id="formreg">
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
                    <input type="text" name="adress" placeholder="Adress" id="adress"/>
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
                    <input type="text" name="position" id="position" placeholder="Position in the company" />
                  </div>
                  <div class="input_field select_option">
                    <select id="country">
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
              </form>
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
 function registration(){
     console.log("Регистрация");
 }
  
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
        <button class="restore" onclick="restore()">Forgot pass?</button>
        
	`;
}

function open_modal_registration()
{
	document.getElementById("Modal").style.display = "block";
	document.getElementById("ModalTitle").innerHTML = ``;
	document.getElementById("ModalBody").innerHTML = `
    <h3 align="center">Registration</h3>
    <div class="form_wrapper">
        <div class="form_container">
          <div class="title_container">
          </div>
          <div class="row clearfix">
            <div class="message">
              <form id="formreg">
                <div class="input_field"> <span><i aria-hidden="true" class="fa fa-envelope"></i></span>
                  <input type="email" name="email" placeholder="Email" id="email" required />
                </div>
                <div class="input_field"> <span><i aria-hidden="true" class="fa fa-lock"></i></span>
                  <input type="password" name="password" placeholder="Password" id="password" required />
                </div>
                <div class="input_field"> <span><i aria-hidden="true" class="fa fa-envelope"></i></span>
                    <input type="text" name="company" placeholder="Company" id="company" required />
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
                  <div class="input_field"> <span><i aria-hidden="true" class="fa fa-envelope"></i></span>
                    <input type="text" name="adress" placeholder="Adress" id="adress" required />
                  </div>
                <div class="row clearfix">
                  <div class="col_half">
                    <div class="input_field"> <span><i aria-hidden="true" class="fa fa-user"></i></span>
                      <input type="number" name="postalcode" maxlength="6" id="postal_code"  placeholder="Postal Code" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"> <span><i aria-hidden="true" class="fa fa-user"></i></span>
                      <input type="text" name="city" id="city" placeholder="City" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"> <span><i aria-hidden="true" class="fa fa-user"></i></span>
                      <input type="number" name="telephone" id="telephone" placeholder="Telephone" />
                    </div>
                  </div>
                  <div class="col_half">
                    <div class="input_field"> <span><i aria-hidden="true" class="fa fa-user"></i></span>
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
                      <input type="text" name="lastname" id="last_name" placeholder="Last Name" required />
                    </div>
                  </div>
                </div>
                <div class="input_field"> <span><i aria-hidden="true" class="fa fa-envelope"></i></span>
                    <input type="text" name="position" id="position" placeholder="Position in the company" required />
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
                  <div class="input_field"> <span><i aria-hidden="true" class="fa fa-envelope"></i></span>
                    <input type="text" name="industry" id="industry" placeholder="Industry in which your company is working" required />
                  </div>
                  <div class="dynamic_fields">
                    <div class="example_student">
                        <div class="table">
                            <div class="cell"><input class="form-control" type="text" name="name[]"/></div>
                            <div class="cell">
                                <button class="js-remove pull-right btn btn-danger">-</button>
                            </div>
                        </div>
                    </div>
                  

                    <div class="students"></div>
                    <button class="js-add pull-right btn btn-success" id="AddBtn">Add Industry</button><br><br><br>
                </div>
    
                <input class="button" type="submit" value="Register" onclick="registratyin()" />
              </form>
            </div>
          </div>
        </div>`;
	
}

function CloseModal()
 {
   document.getElementById("Modal").style.display = "none";
 }

 function restore(){
     prompt("Забыли пароль?");
 }
 function registration(){
     console.log("Регистрация");
 }
  
$(document).ready(function(){

    $("#login").on('click',function(){
        html = `<div class='col mt-2'>
            <div class='form-group'>
                <label class='label' for='username'> Username</label>
                <input type="text" class='form-control ml-3'  id="username" placeholder="Enter Username" name="username" />
            </div>
        </div>
            <div class='col mt-2'>
                <div class='form-group'>
                    <label class='label'> Password </label>
                     <input type="Password" class='form-control ml-3'  id="password" placeholder="Enter Password" name='password'/>
                </div>
        </div>
        <div class='col mt-2'>
            <div class='form-group'>
                <button type="submit" class="btn btn-success btn-sm" name="login_btn">Login</button>
                Don't have any account? <button class="btn btn-info btn-sm" id="signupp" name="signup_btn">SignUp</button>
            </div>
            
        </div>`

        $("#form").html(html)
    })

    $("#signupp").on('click',function(){
        html = `<div class='col mt-2'>
        <div class='form-group' id="user_check">                                 
            <label class='label' for='username'> Username </label><span class="ml-3" id="check_user" style="color:pink;display:none">Checking Availability...</span>
            <input type="text" class='form-control ml-3'  id="username" placeholder="Enter Username" name=" " />
            <span id="status"></span>
            
        </div>
    </div>
    <div class='col mt-2'>
        <div class='form-group'>
            <label class='label'> First Name </label>
            <input type="text" class='form-control ml-3'  id="first" placeholder=" Enter First Name" name='first_name' />
        </div>
    </div><div class='col mt-2'>
        <div class='form-group'>
            <label class='label'> Last Name </label>
            <input type="text" class='form-control ml-3'  id="last" placeholder=" Enter Last Name"name='last_name'/>
        </div>
    </div><div class='col mt-2'>
        <div class='form-group'>
            <label class='label'> Email </label><span class="ml-3" id="check_email" style="color:pink;display:none">Checking Availability...</span>
            <input type="text" class='form-control ml-3'  id="email" placeholder="Enter Email" name='email'/>
        </div>
    </div>
        <div class='col mt-2'>
            <div class='form-group'>
                <label class='label'> Password </label>
                 <input type="Password" class='form-control ml-3'  id="password" placeholder="Enter Password" name='password1'/>
            </div>
    </div>
    <div class='col mt-2'>
        <div class='form-group'>
            <label class='label'> Retype Password </label>
            <input type="password" class='form-control ml-3'  id="password2" placeholder="Confirm Password" name="password2"/>
        </div>
    </div>
    <div class='col mt-2'>
        <div class='form-group'>
            <button type="submit" class="btn btn-success btn-sm" name="signup_btn">Sign Up</button>
            Already have an Account?  <button class="btn btn-info btn-sm" id="login" name="login_btn">Login</button>
        </div>
        
    </div>`

        $("#form").html(html)
    })

    setTimeout(function () {
        if ($('#msg').length > 0) {
            $('#msg').slideUp(900, function () {
                $("#msg").remove();
            });
        }
    }, 5000)

    function show_u(){
        $("#check_user").css('display','inline')
    }
    function hide_u(){
        $("#check_user").css('display','none')
    }
    function show_e(){
        $("#check_email").css('display','inline')
    }
    function hide_e(){
        $("#check_email").css('display','none')
    }
    
    $("#username").keyup(function(e){
        show_u()
        data = e.target.value
        $.ajax({
            url : `check/${data}`,
            type :'GET',
            success : function(res){
                if(res.status == 0){
                    hide_u()
                    html = `<small id="emailHelp" class="form-text text-danger">This username Already Exists, please Choose Another One</small>`
                    $("#status").html(html)
                }else if(res.status == 1){
                    hide_u()
                    html = `<small id="emailHelp" class="form-text text-success">Username is Available</small>`
                    $("#status").html(html)
                }else if(res.status == 2){
                    hide_u()
                    html = `<small id="emailHelp" class="form-text text-Info">Username length Should Be minimum of 6 characters</small>`
                    $("#status").html(html)
                }
            }
        })
    })

    $("#email").keyup(function(e){
        show_e()
        data = e.target.value
        $.ajax({
            url : `check/${data}`,
            type :'GET',
            success : function(res){
                if(res.status == 0){
                    hide_e()
                    html = `<small id="emailHelp" class="form-text text-danger">This Email Already Exists, You can login to account.</small>`
                    $("#status").html(html)
                }else if(res.status == 1){
                    hide_e()
                    html = ''
                    $("#status").html(html)
                }else if(res.status == 2){
                    hide_e()
                    html = `<small id="emailHelp" class="form-text text-Info">Enter Valid Email Id</small>`
                    $("#status").html(html)
                }
            }
        })
    })

    $("#password2").keyup(function(){
        p1 = $("#password1").val()
        p2 = $(this).val()
        if(p1 == p2){
            $("#password1").css('border-width','1px');
            $("#password1").css('border-color','#ced4da');
            $(this).css('border-width','1px');
            $(this).css('border-color','#ced4da')
            // return true
        } else {
            $("#password1").css('border-width','3px')
            $("#password1").css('border-color','red')
            $(this).css('border-width','3px')
            $(this).css('border-color','red')

        }
    })








})
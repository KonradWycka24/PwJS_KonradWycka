        var err=false;
        var imie = document.getElementById('Fimie');
        var nazwisko = document.getElementById('Fnazwisko');
        var email = document.getElementById('Femail');
        var informacja = document.getElementById('Finformacja');
        var info = informacja.value;
        var eemail = email.value;
        var regex = /^[a-zA-Z0-9._-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z0-9.-]{2,4}$/;
        form.addEventListener('submit', e => {
            e.preventDefault();
        checkForm();
        });

function checkForm() 
{

        if (imie.value=="")
        {
            document.getElementById('errorImie').className='alert alertdanger';
            document.getElementById('fgimie').className='form-group has-error has-feedback';
            document.getElementById('icoimie').className='glyphicon glyphicon-remove form-control-feedback';
            err = true;
        }
        else 
        {
            document.getElementById('fgimie').className='form-group has-success has-feedback';
            document.getElementById('icoimie').className='glyphicon glyphicon-ok form-control-feedback';
        }

        if (nazwisko.value=="")
        {
            document.getElementById('errorNazwisko').className='alert alertdanger';
            document.getElementById('fgnazwisko').className='form-group has-error has-feedback';
            document.getElementById('iconaz').className='glyphicon glyphicon-remove form-control-feedback';
            err = true;
        }
        else
        {
            document.getElementById('fgnazwisko').className='form-group has-success has-feedback';
            document.getElementById('iconaz').className='glyphicon glyphicon-ok form-control-feedback';
        }

        if (email.value=="")
        {
            document.getElementById('errorEmail').className='alert alertdanger';
            document.getElementById('fgemail').className='form-group has-error has-feedback';
            document.getElementById('icoema').className='glyphicon glyphicon-remove form-control-feedback';
            err = true;
        } else if (regex.test(eemail)== false)
        {
                document.getElementById('errorEmail').className='alert alertdanger';
                document.getElementById('fgemail').className='form-group has-error has-feedback';
                document.getElementById('icoema').className='glyphicon glyphicon-remove form-control-feedback';
                err= true;
            }
        else {
            document.getElementById('fgemail').className='form-group has-success has-feedback';
            document.getElementById('icoema').className='glyphicon glyphicon-ok form-control-feedback';
        }
        
        if (info.length < 250)
        {
            document.getElementById('errorInfo').className='alert alertdanger';
            document.getElementById('fginfo').className='form-group has-error has-feedback';
            document.getElementById('icoinfo').className='glyphicon glyphicon-remove form-control-feedback';
            err=true;
        }
        else {
            document.getElementById('fginfo').className='form-group has-success has-feedback';
            document.getElementById('icoinfo').className='glyphicon glyphicon-ok form-control-feedback';
        }

     
}
function blurImie()
{
  if (imie.value=="")
  {
      document.getElementById('errorImie').className='alert alertdanger';
      document.getElementById('fgimie').className='form-group has-error has-feedback';
      document.getElementById('icoimie').className='glyphicon glyphicon-remove form-control-feedback';
      err = true;
  }
  else 
  {
    document.getElementById('errorImie').className='hide';
      document.getElementById('fgimie').className='form-group has-success has-feedback';
      document.getElementById('icoimie').className='glyphicon glyphicon-ok form-control-feedback';
  }
}

function blurNazw()
{
    if (nazwisko.value=="")
    {
        document.getElementById('errorNazwisko').className='alert alertdanger';
        document.getElementById('fgnazwisko').className='form-group has-error has-feedback';
        document.getElementById('iconaz').className='glyphicon glyphicon-remove form-control-feedback';
        err = true;
    }
    else
    {
        document.getElementById('errorNazwisko').className='hide';
        document.getElementById('fgnazwisko').className='form-group has-success has-feedback';
        document.getElementById('iconaz').className='glyphicon glyphicon-ok form-control-feedback';
    }
}
function blurEmail()
{
    if (email.value=="")
        {
            document.getElementById('errorEmail').className='alert alertdanger';
            document.getElementById('fgemail').className='form-group has-error has-feedback';
            document.getElementById('icoema').className='glyphicon glyphicon-remove form-control-feedback';
            err = true;
        } else if (regex.test(eemail)== false)
        {
                document.getElementById('errorEmail').className='alert alertdanger';
                document.getElementById('fgemail').className='form-group has-error has-feedback';
                document.getElementById('icoema').className='glyphicon glyphicon-remove form-control-feedback';
                err= true;
            }
        else {
            document.getElementById('errorEmail').className='hide';
            document.getElementById('fgemail').className='form-group has-success has-feedback';
            document.getElementById('icoema').className='glyphicon glyphicon-ok form-control-feedback';
        }
}
function blurInfo()
{
    if (info.length < 250)
    {
        document.getElementById('errorInfo').className='alert alertdanger';
        document.getElementById('fginfo').className='form-group has-error has-feedback';
        document.getElementById('icoinfo').className='glyphicon glyphicon-remove form-control-feedback';
        err=true;
    }
    else {
        document.getElementById('errorInfo').className='hide';
        document.getElementById('fginfo').className='form-group has-success has-feedback';
        document.getElementById('icoinfo').className='glyphicon glyphicon-ok form-control-feedback';
    }

}
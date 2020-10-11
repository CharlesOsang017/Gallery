

  $(function() {
    $("input").click(function() {
    $(this).focus();
    $(this).select();
    document.execCommand('copy');
    $(this).after("Copied to clipboard");
    });
   });
# includefile-blockchain

In this implementation, the HTML page contains a textarea where users can input data to append to the blockchain. The JavaScript code uses the fetch() API to make a POST request to the server-side Perl script at the /appendData endpoint. Upon receiving a response, it updates the status message on the page to inform the user about the result of the data inclusion operation. Note that you would need to set up a server to handle the POST request and interact with the includefile subroutine on the backend.

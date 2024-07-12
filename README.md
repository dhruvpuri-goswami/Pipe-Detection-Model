# Connection Setup
If we have Django Server and wants to connect with Android Java Application then follow these steps:
- 1st in Android-Java, write following code if you use OkHttp
```java
protected void postRequest(byte[] imageData){
        Toast.makeText(this, "Making Post Request", Toast.LENGTH_SHORT).show();
        RequestBody reqBody = new MultipartBody.Builder()
                .setType(MultipartBody.FORM)
                .addFormDataPart("image", "image.png", RequestBody.create(MediaType.parse("image/png"), imageData))
                .build();

        Request request = new Request.Builder()
        // Now, Url should with prefix: "https://" otherwise it will give this Error: "Android 8: Cleartext HTTP traffic not permitted"
        // Solution is not just "https://", there are also other: https://stackoverflow.com/a/50834600/13735044
        // I tried this one and runned successfully: android:usesCleartextTraffic="true" in <application /> tag of AndroidManifest.xml
                .url("http://HOST_URL:PORT/api/detect/")
                .post(reqBody)
                .build();

        Toast.makeText(this, "Request Body done", Toast.LENGTH_SHORT).show();

        // !!!! Now, Here only enqueue(callback) is perfect running way to send post request. Instead of Response response = client.newCall(request).execute(); 
        // Why you must use enqueue() method: https://stackoverflow.com/a/28135573/13735044
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                Log.d("Error", e.toString());
                // !!!! Don't put Toast here, it won't executed
            }

            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
                Log.d("Success", response.body().string());
                // !!!! Don't put Toast here, it won't executed
            }
        });

//      This following way not work.  
//      try {
//            Toast.makeText(this, "Done???", Toast.LENGTH_SHORT).show();
//            Response response = client.newCall(request).execute();
//            if (!response.isSuccessful()){
//                Log.d("Error", String.valueOf(response));
//                Toast.makeText(this, response.toString() + " unexpected", Toast.LENGTH_SHORT).show();
//                throw new IOException("Unexpected code " + response);
//            }
//            Toast.makeText(this, response.body().string(), Toast.LENGTH_SHORT).show();
//        } catch (IOException e) {
//            Log.e("ERROR", e.toString());
//            Toast.makeText(this, e.toString(), Toast.LENGTH_SHORT).show();
//            throw new RuntimeException(e);
//        } catch (Exception e){
//            Log.e("ERROR", e.toString());
//            Toast.makeText(this, e.toString(), Toast.LENGTH_SHORT).show();
//        }
    }
```


- 2nd thing, Don't Forget to mention following in AndroidManifest.xml
```xml
<uses-permission android:name="android.permission.INTERNET" />
```
- 3rd thing To test in mobile, Your PC and Mobile Device should be in single network.
    - Connect Your PC with Mobile Hostpot Connection
    - Now check IP using ipconfig
    - Now run your python server by CUSTOME_URL `python manage.py runserver <Your_IP_FROM_IPCONFIG>:<ANY_OPEN_PORT>`
        - Example: `python manage.py runserver XXX.XXX.XXX.XXX:PORT`
    - Now, We have to set `ALLOWED_HOSTS` Array in `settings.py`
        - ALLOWED_HOSTS = ['Your_IP_FROM_IPCONFIG']
        - Solutions: https://stackoverflow.com/a/40582485
    - Now, Specify DJANGO LIVE SERVER URL in android-java.
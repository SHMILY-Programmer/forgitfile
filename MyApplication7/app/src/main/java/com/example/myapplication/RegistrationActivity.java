package com.example.myapplication;

import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Environment;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.RandomAccessFile;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.Date;

public class RegistrationActivity extends AppCompatActivity {
    MediaRecorder mediaRecorder;
    Button btn1;
    AudioUtil util=AudioUtil.getInstance();
    String s=null;
//    String mFileName1=getExternalFilesDir(null)+"/";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);
        btn1 = (Button) findViewById(R.id.login);

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CharSequence text = btn1.getText();
                //姓名学号不能为空，本来还应该匹配的，先不做匹配的工作
                EditText name = findViewById(R.id.text1);
                EditText num = findViewById(R.id.text2);
                String s1 = name.getText().toString().trim();
                String s2 = num.getText().toString().trim();
//                info=new SaveMessageInfo();
                String sb=null;
                if (TextUtils.equals(text, "注册") && !TextUtils.isEmpty(s1) && !TextUtils.isEmpty(s2)) {


                    btn1.setText("结束");
      /*              mediaRecorder = new MediaRecorder();
                    mediaRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);//设置音频
                    mediaRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);

                    String mFileName = getExternalFilesDir(null) + "/rcd_";
//                    String mFileName = "/storage/emulated/0/Android/data.com.example.myapplication/file/rcd_";

                    String s = new SimpleDateFormat("yyyy-MM-dd hhmmss")
                            .format(new Date());
                    mFileName += s + ".3gp";
                    mediaRecorder.setOutputFile(mFileName);
                    mediaRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);

*/
                    //采用audiorecoder
                    s = new SimpleDateFormat("yyyy-MM-dd hhmmss")
                            .format(new Date());
                    String mFileName1=getExternalFilesDir(null)+"/";

                    util.startRecord(s,mFileName1);
                    util.recordData();


                 /*   try {
                        mediaRecorder.prepare();
                    } catch (IOException e) {
                    }
                    mediaRecorder.start();*/
                }
                else if (TextUtils.equals(text, "注册") && TextUtils.isEmpty(s1) && !TextUtils.isEmpty(s2)) {
                    new AlertDialog.Builder(RegistrationActivity.this)
                            .setTitle("提示")
                            .setMessage("请输入姓名~")
                            .setPositiveButton("确定", null)
                            .show();
                }
                else if (TextUtils.equals(text, "注册") && !TextUtils.isEmpty(s1) && TextUtils.isEmpty(s2)) {
                    new AlertDialog.Builder(RegistrationActivity.this)
                            .setTitle("提示")
                            .setMessage("请输入学号~")
                            .setPositiveButton("确定", null)
                            .show();
                }
                else if (TextUtils.equals(text, "注册") && TextUtils.isEmpty(s1) && TextUtils.isEmpty(s2)) {
                    new AlertDialog.Builder(RegistrationActivity.this)
                            .setTitle("提示")
                            .setMessage("请输入姓名和学号~")
                            .setPositiveButton("确定", null)
                            .show();
                }
                else if (TextUtils.equals(text, "结束")) {

                    btn1.setText("注册");
                    String mFileName1=getExternalFilesDir(null)+"/";

                    util.stopRecord();
                    util.convertWaveFile(s,mFileName1);

                   /* mediaRecorder.stop();
                    mediaRecorder.release();
                    mediaRecorder = null;*/
                    final String h=null;
                    try {
                        //  fileUpload();
                        new Thread(new Runnable() {
                            @Override
                            public void run() {
                                try {
                                    for (int i=0;i<10;i++){
                                    fileUpload(s1,s);
                                    }
                                  register(s1);
                                    showDialog();
                                    Toast.makeText(RegistrationActivity.this, "You clicked Button 1", Toast.LENGTH_SHORT).show();

                                } catch (Exception e) {
                                    e.printStackTrace();
                                }
                            }
                        }
                        ).start();
                        System.out.println(h);


                    } catch (Exception e) {
                        e.printStackTrace();
                    }

                }

            }
        });
    }

    String getFiles(String filename) {
        File path = null;
        path = getExternalFilesDir(null);
        ///storage/emulated/0/Android/data/com.example.myapplication/files/
        File[] files = path.listFiles();
        for (File file : files) {
            file.getPath();
            String s = file.getPath().substring(file.getPath().lastIndexOf("/") + 1);
            if (s != null && file.getPath() != null && file.getPath().substring(file.getPath().lastIndexOf("/") + 1).equals(filename+".wav")) {
                //实际上要把刚注册的人的语音上传即可

                return file.getPath();
            }
        }
        return null;
    }

    /*
    文件上传到服务器
     */
   void fileUpload(String sname,String filename) throws Exception {
//       URL url = new URL("http://192.168.43.68:8090/SRAPP3-1.0-SNAPSHOT/FileUpload");
//       HttpURLConnection connection = (HttpURLConnection) url.openConnection();
//       connection.setRequestMethod("GET");//获取服务器数据
//       connection.setReadTimeout(8000);//设置读取超时的毫秒数
//       connection.setConnectTimeout(8000);//设置连接超时的毫秒数
//       InputStream in = connection.getInputStream();
//       BufferedReader reader = new BufferedReader(new InputStreamReader(in));
//       String result = reader.readLine();//读取服务器进行逻辑处理后页面显示的数据
//       Log.d("MainActivity","run: "+result);

//       SharedPreferences mSharedPreferences = null;
//       mSharedPreferences.getString("content","");

        String end = "\r\n";
        String twoHyphens = "--";
        String boundary = "*****";
        String srcPath = getFiles(filename);
        URL url = new URL("http://192.168.43.68:8090/SRAPP3-1.0-SNAPSHOT/FileUpload?name="+sname);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();


        /* 允许Input、Output，不使用Cache */

        con.setDoInput(true);
        con.setDoOutput(true);
        con.setUseCaches(false);
        /* 设置传送的method=POST */
        con.setRequestMethod("POST");
        /* setRequestProperty */

        con.setRequestProperty("Connection", "Keep-Alive");
        con.setRequestProperty("Charset", "UTF-8");
        con.setRequestProperty("Content-Type", "multipart/form-data;boundary="
                + boundary);
        con.setReadTimeout(8000);
        con.setConnectTimeout(8000);

        /* 设置DataOutputStream */
        DataOutputStream ds = new DataOutputStream(con.getOutputStream());
        ds.writeBytes(twoHyphens + boundary + end);
        ds.writeBytes("Content-Disposition: form-data; "
                + "name=\"file1\";filename=\"" + srcPath.substring(srcPath.lastIndexOf("/") + 1) + "\"" + end);
        ds.writeBytes(end);


        /* 取得文件的FileInputStream */
        FileInputStream fStream = new FileInputStream(srcPath);
        /* 设置每次写入8192bytes */
        int bufferSize = 1024;
        byte[] buffer = new byte[bufferSize];

        int length = -1;
        /* 从文件读取数据至缓冲区 */
        while ((length = fStream.read(buffer)) != -1) {
            /* 将资料写入DataOutputStream中 */
            ds.write(buffer, 0, length);
            Log.i("tag","ok");
        }
        ds.writeBytes(end);
        ds.writeBytes(twoHyphens + boundary + twoHyphens + end);

        /* close streams */
        fStream.close();
        ds.flush();
        String name=null;
        /* 取得Response内容  从服务器端发回的数据*/
        InputStream is = con.getInputStream();
        int ch;
        StringBuffer b = new StringBuffer();
        while ((ch = is.read()) != -1) {
            b.append((char) ch);//最后留的b就是对应的识别出的说话人
            System.out.println(b);

            Log.i("tag","oker");
        }


        /* 关闭DataOutputStream */
        ds.close();


    }
   String register(String sname) throws IOException {
       URL url = new URL("http://192.168.43.68:8090/SRAPP3-1.0-SNAPSHOT/Register?name="+sname);
       HttpURLConnection con = (HttpURLConnection) url.openConnection();
       InputStream is = con.getInputStream();
       int ch;
       StringBuffer b = new StringBuffer();
       while ((ch = is.read()) != -1) {
           b.append((char) ch);//最后留的b就是对应的识别出的说话人
           System.out.println(b);
           Log.i("tag1","oker");
       }
       String sb=b.toString();
       return sb;


   }
    private void showDialog(){
        AlertDialog.Builder builder=new AlertDialog.Builder(this);
        builder.setMessage("注册成功！");
        builder.setPositiveButton("我知道了", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {

            }
        });
        AlertDialog dialog=builder.create();
        dialog.show();



    }


}



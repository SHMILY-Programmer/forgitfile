package com.example.myapplication;

import android.content.DialogInterface;
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

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Objects;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class LoginActivity extends AppCompatActivity {

    Button btn1;
    MediaRecorder mediaRecorder ;
    AudioUtil util=AudioUtil.getInstance();
    String s=null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        btn1 = (Button) findViewById(R.id.login);
        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CharSequence text=btn1.getText();
                EditText name=findViewById(R.id.text3);
                EditText num=findViewById(R.id.text4);
                String s1=name.getText().toString().trim();
                String s2=num.getText().toString().trim();
                if(TextUtils.equals(text,"打卡")&&!TextUtils.isEmpty(s1)&&!TextUtils.isEmpty(s2)) {
                    btn1.setText("结束");
                    //showDialog();
                    // SoundRecorder soundRecorder=new SoundRecorder();
                    //soundRecorder.startRecording();
                    mediaRecorder = new MediaRecorder();
              //      mediaRecorder.reset();
                    mediaRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);//设置音频
                   // mediaRecorder.setVideoSource(MediaRecorder.VideoSource.CAMERA);
                    mediaRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
              //      mediaRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AAC);

                    //mediaRecorder.setOrientationHint(90);
                    String mFileName1 = getExternalFilesDir(null)+"/";

                    s = new SimpleDateFormat("yyyy-MM-dd hhmmss")
                            .format(new Date());

                    util.startRecord(s,mFileName1);
                    util.recordData();

                    // SDCard地址 /storage/emulated/0
                    // getExternalStorageDirectory在29已废弃
//  String saveDir = Environment.getExternalStorageDirectory().getAbsolutePath();
                    // getExternalFilesDir() 用于获取SDCard/Android/data/你的应用的包名/files/ 目录
//                    File externalFileRootDir = getExternalFilesDir(null);
//                    do {
//                        externalFileRootDir = Objects.requireNonNull(externalFileRootDir).getParentFile();
//                    } while (Objects.requireNonNull(externalFileRootDir).getAbsolutePath().contains("/Android"));
//
//                    String saveDir = Objects.requireNonNull(externalFileRootDir).getAbsolutePath();
//                    String savePath = saveDir + "/" + Environment.DIRECTORY_DCIM + "/" + mFileName;


//                    mediaRecorder.setOutputFile(mFileName);
                   // mediaRecorder.setOutputFile(new File(getExternalFilesDir(""),"a.mp4").getAbsolutePath());
//                    mediaRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
                    //mediaRecorder.setVideoSize(640,480);
//
//                   try {
////                        mediaRecorder.prepare();
//                    } catch (IOException e) {
//                       // showDialog();
//                    }
////                    mediaRecorder.start();
                }
                else if(TextUtils.equals(text,"打卡")&&TextUtils.isEmpty(s1)&&!TextUtils.isEmpty(s2)){
                    new AlertDialog.Builder(LoginActivity.this)
                            .setTitle("提示")
                            .setMessage("请输入姓名~")
                            .setPositiveButton("确定",null)
                            .show();
                }
                else if(TextUtils.equals(text,"打卡")&&!TextUtils.isEmpty(s1)&&TextUtils.isEmpty(s2)){
                    new AlertDialog.Builder(LoginActivity.this)
                            .setTitle("提示")
                            .setMessage("请输入学号~")
                            .setPositiveButton("确定",null)
                            .show();
                }
                else if(TextUtils.equals(text,"打卡")&&TextUtils.isEmpty(s1)&&TextUtils.isEmpty(s2)){
                    new AlertDialog.Builder(LoginActivity.this)
                            .setTitle("提示")
                            .setMessage("请输入姓名和学号~")
                            .setPositiveButton("确定",null)
                            .show();
                }
                else if(TextUtils.equals(text,"结束")){
                    btn1.setText("打卡");
//                    mediaRecorder.stop();
//                    mediaRecorder.release();
//                    mediaRecorder = null;
                    String mFileName1 = getExternalFilesDir(null)+"/";
                    util.stopRecord();
                    util.convertWaveFile(s,mFileName1);

//                    MythreadReturn1 mythreadReturn=new MythreadReturn1(mFileName1,s1,s);
                    FutureTask task=new FutureTask(new MythreadReturn1(mFileName1,s1,s));
                    Thread thread=new Thread(task);
//                    new Thread(task).start();
                    thread.start();
                    try {
                        System.out.println("hhh"+task.get());

                        if (task.get().equals("true"))
                            showDialog("打卡成功！");
                        else {
                            showDialog("非本人，请重新打卡！");
                        }
                        thread.sleep(2000);
                    } catch (ExecutionException e) {
                        e.printStackTrace();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
//                    String sb=null;
//                    Thread thread=new Thread(new Runnable() {
//                        String sb=null;
//                        @Override
//                        public void run() {
//                            try {
//                              sb=login(mFileName1,s1,s);
//                            } catch (Exception e) {
//                                e.printStackTrace();
//                            }
//                        }
//                        public String getvalue(){
//                            return sb;
//                        }
//                    });
//                    thread.start();
//                    Thread thread1=new Thread(thread);
//                    thread1.start();
//thread1.getvalue();
//                    try {
//                        thread.sleep(3000);
//                    } catch (InterruptedException e) {
//                        e.printStackTrace();
//                    }                 if

                }
            }
        }
        );
    }
    String  login(String filepath,String sname,String filename) throws Exception {
        String end = "\r\n";
        String twoHyphens = "--";
        String boundary = "*****";
        String srcPath = getFiles(filepath,filename);
        URL url = new URL("http://192.168.43.68:8090/SRAPP3-1.0-SNAPSHOT/Login?name="+sname);
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
        con.setReadTimeout(80000);
        con.setConnectTimeout(80000);

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
        if (b.equals("true")){
            showDialog("打卡成功");
        }
        else {
            showDialog("打卡失败");
        }
        Toast.makeText(LoginActivity.this, "You clicked Button 1", Toast.LENGTH_SHORT).show();

        /* 关闭DataOutputStream */
        ds.close();
        String sb=b.toString();
        return  sb;

    }
    String getFiles(String filepath,String filename) {
        File path = null;
        path=new File(filepath);
//        path = getExternalFilesDir(null);
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
    private void showDialog(String say){
        AlertDialog.Builder builder=new AlertDialog.Builder(LoginActivity.this);
        builder.setMessage(say);
        builder.setPositiveButton("我知道了", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {

            }
        });
        AlertDialog dialog=builder.create();
        dialog.show();



    }
}

class MythreadReturn implements Runnable{
    String sb=null;
    String s1,s,filepath;
    public MythreadReturn(String s1,String s,String filepath){
        this.s1=s1;
        this.s=s;
        this.filepath=filepath;
    }
    @Override
    public void run() {
        try {
            sb=login(s1,s,filepath);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public String getValue(){
        return sb;
    }
    String  login(String filepath,String sname,String filename) throws Exception {
        String end = "\r\n";
        String twoHyphens = "--";
        String boundary = "*****";
        String srcPath = getFiles(filename,filepath);
        URL url = new URL("http://192.168.43.68:8090/SRAPP3-1.0-SNAPSHOT/Login?name="+sname);
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
        con.setReadTimeout(80000);
        con.setConnectTimeout(80000);

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
        if (b.equals("true")){
//            showDialog("打卡成功");
        }
        else {
//            showDialog("打卡失败");
        }

        /* 关闭DataOutputStream */
        ds.close();
        String sb=b.toString();
        System.out.println("sb"+sb);
        return  sb;

    }
    String getFiles(String filename,String paths) {
        File path = null;
        path=new File(paths);
//        path = getExternalFilesDir(null);
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

}
class MythreadReturn1 implements Callable {
    String sb=null;
    String s1,s,filepath;
    public MythreadReturn1(String s1,String s,String filepath){
        this.s1=s1;
        this.s=s;
        this.filepath=filepath;
    }

    String  login(String filepath,String sname,String filename) throws Exception {
        String end = "\r\n";
        String twoHyphens = "--";
        String boundary = "*****";
        String srcPath = getFiles(filename,filepath);
        URL url = new URL("http://192.168.43.68:8090/SRAPP3-1.0-SNAPSHOT/Login?name="+sname);
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
        con.setReadTimeout(80000);
        con.setConnectTimeout(80000);

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
        if (b.equals("true")){
//            showDialog("打卡成功");
        }
        else {
//            showDialog("打卡失败");
        }

        /* 关闭DataOutputStream */
        ds.close();
        String sb=b.toString();
        System.out.println("sb"+sb);
        return  sb;

    }
    String getFiles(String filename,String paths) {
        File path = null;
        path=new File(paths);
//        path = getExternalFilesDir(null);
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

    @Override
    public Object call() throws Exception {
        sb=login(s1,s,filepath);
        return sb;
    }
}
//class SoundRecorder {
//
//    MediaRecorder mRecorder;
//
//                  boolean isRecording;
//                  public void startRecording() {
//                  mRecorder = new MediaRecorder();
//                     mRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
//                     mRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
//                     mRecorder.setOutputFile(newFileName());
//                     mRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
//                     try {
//                             mRecorder.prepare();
//                         } catch (IOException e) {
//
//                         }
//                   mRecorder.start();
//
//
//
//
//                 }
//
//                 public void stopRecording() {
//                     mRecorder.stop();
//                     mRecorder.release();
//                     mRecorder = null;
//                 }
//
//                 public String newFileName() {
//                     String mFileName = Environment.getExternalStorageDirectory()
//                             .getAbsolutePath();
//
//                     String s = new SimpleDateFormat("yyyy-MM-dd hhmmss")
//                             .format(new Date());
//                     return mFileName += "/rcd_" + s + ".3gp";
//                 }
//     }



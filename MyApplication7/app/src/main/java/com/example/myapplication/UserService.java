package com.example.myapplication;

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.net.URLEncoder;

public class UserService {
//    public static boolean signIn(String name,String password){
//MyThread myThread=new MyThread("http://192.168.0.111:8090/SRAPP3-1.0-SNAPSHOT/",name,password);
//    }
}
//class MyThread extends Thread{
//
//
//    @Override
//    public void run(){
//        String end="\r\n";
//        String twoHyphens="--";
//        String boundary="*****";
//        String srcPath=getFiles();
//        URL url= null;
//        try {
//            url = new URL("http://192.168.0.111:8090/SRAPP3-1.0-SNAPSHOT/FileUpload");
//        } catch (MalformedURLException e) {
//            e.printStackTrace();
//        }
//
//        HttpURLConnection con= null;
//        try {
//            con = (HttpURLConnection) url.openConnection();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        con.setDoInput(true);
//        con.setDoOutput(true);
//        con.setUseCaches(false);
//        try {
//            con.setRequestMethod("POST");
//        } catch (ProtocolException e) {
//            e.printStackTrace();
//        }
//        con.setRequestProperty("Connection","Keep-Alive");
//        con.setRequestProperty("Charset","UTF-8");
//        con.setRequestProperty("Content-Type","multipart/form-data;boundary="+boundary);
//        DataOutputStream ds= null;
//        try {
//            ds = new DataOutputStream(con.getOutputStream());
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        try {
//            ds.writeBytes(twoHyphens+boundary+end);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        try {
//            ds.writeBytes("Content-Disposition:form-data;"+"name=\"file\";filename=\""+srcPath.substring(srcPath.lastIndexOf("/")+1)+"\""+end);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        try {
//            ds.writeBytes(end);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//
//        FileInputStream fstream= null;
//        try {
//            fstream = new FileInputStream(srcPath);
//        } catch (FileNotFoundException e) {
//            e.printStackTrace();
//        }
//        int bufferSize=8192;
//        byte[] buffer=new byte[bufferSize];
//        int length=-1;
//        while(true){
//            try {
//                if (!((length=fstream.read(buffer))!=-1)) break;
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            try {
//                ds.write(buffer,0,length);
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//        }
//        try {
//            ds.writeBytes(end);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        try {
//            ds.writeBytes(twoHyphens+boundary+twoHyphens+end);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//
//        try {
//            fstream.close();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        try {
//            ds.flush();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//
//        InputStream is= null;
//        try {
//            is = con.getInputStream();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        int ch;
//        StringBuffer b=new StringBuffer();
//        while(true){
//            try {
//                if (!((ch=is.read())!=-1)) break;
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            b.append((char)ch);
//
//        }
//        try {
//            ds.close();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }
//}



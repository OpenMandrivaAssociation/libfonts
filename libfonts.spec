Name:           libfonts
Version:        1.1.6
Release:        %mkrel 3
Summary:        TrueType Font Layouting
License:        LGPLv2+
Group:          System/Libraries 
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
URL:            http://reporting.pentaho.org/
BuildRequires:  ant, ant-contrib, ant-nodeps, java-devel >= 0:1.6.0, jpackage-utils, libloader >= 1.1.3, itext, java-rpmbuild
Requires:       java >= 0:1.6.0, jpackage-utils, libloader >= 1.1.3, itext
BuildArch:      noarch
Patch0:         libfonts-1.1.2-fix-build.patch

%description
LibFonts is a library developed to support advanced layouting in JFreeReport.
This library allows to read TrueType-Font files to extract layouting specific
informations.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation 
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
%patch0 -p0
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase commons-logging-api libloader itext
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p %{buildroot}%{_javadir}
cp -p ./dist/%{name}-%{version}.jar %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sat Jan 12 2013 umeabot <umeabot> 1.1.6-3.mga3
+ Revision: 357116
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Oct 14 2012 ennael <ennael> 1.1.6-2.mga3
+ Revision: 305444
- Documentation group

* Sat Jan 21 2012 kamil <kamil> 1.1.6-1.mga2
+ Revision: 198963
- new version 1.1.6
- rediff and rename patch fix-build.patch
- drop gcj support
- clean .spec

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.3-3.mga1
+ Revision: 74326
- Really build without gcj

* Wed Jan 26 2011 dmorgan <dmorgan> 1.1.3-2.mga1
+ Revision: 40204
- Fix requires

* Wed Jan 26 2011 dmorgan <dmorgan> 1.1.3-1.mga1
+ Revision: 40128
- Adapt for mageia
- imported package libfonts


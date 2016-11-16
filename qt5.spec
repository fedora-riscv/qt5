
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name: qt5
Version: 5.6.2
Release: 1%{?dist}
Summary: Qt5 meta package
License: GPLv3
URL: https://getfedora.org/
Source0: macros.qt5
Source1: macros.qt5-srpm
BuildArch: noarch
Requires: qt5-gstreamer
Requires: qt5-qdbusviewer
Requires: qt5-qt3d
Requires: qt5-qtaccountsservice
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: qt5-qtbase-mysql
Requires: qt5-qtbase-postgresql
Requires: qt5-qtconfiguration
Requires: qt5-qtconnectivity
Requires: qt5-qtdeclarative
Requires: qt5-qtdoc
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtimageformats
Requires: qt5-qtlocation
Requires: qt5-qtmultimedia
Requires: qt5-qtquickcontrols
Requires: qt5-qtquickcontrols2
Requires: qt5-qtscript
Requires: qt5-qtsensors
Requires: qt5-qtserialport
Requires: qt5-qtsvg
Requires: qt5-qttools
Requires: qt5-qtwayland
Requires: qt5-qtwebchannel
#Requires: qt5-qtwebengine
Requires: qt5-qtwebkit
Requires: qt5-qtwebsockets
Requires: qt5-qtx11extras
Requires: qt5-qtxmlpatterns

%description
%{summary}.

%package devel
Summary: Qt5 meta devel package
Requires: qt5-qttools-static
Requires: qt5-qtdeclarative-static
Requires: qt5-qtbase-static
Requires: qt5-designer
Requires: qt5-qdoc
Requires: qt5-qhelpgenerator
Requires: qt5-linguist
Requires: qt5-gstreamer-devel
Requires: qt5-qt3d-devel
Requires: qt5-qtaccountsservice-devel
Requires: qt5-qtbase-devel
Requires: qt5-qtconfiguration-devel
Requires: qt5-qtconnectivity-devel
Requires: qt5-qtdeclarative-devel
Requires: qt5-qtenginio-devel
Requires: qt5-qtlocation-devel
Requires: qt5-qtmultimedia-devel
Requires: qt5-qtscript-devel
Requires: qt5-qtsensors-devel
Requires: qt5-qtserialport-devel
Requires: qt5-qtsvg-devel
Requires: qt5-qttools-devel
Requires: qt5-qtwayland-devel
Requires: qt5-qtwebchannel-devel
#Requires: qt5-qtwebengine-devel
Requires: qt5-qtwebkit-devel
Requires: qt5-qtwebsockets-devel
Requires: qt5-qtx11extras-devel
Requires: qt5-qtxmlpatterns-devel

%description devel
%{summary}.

%package rpm-macros
Summary: Qt5 RPM macros for KDE Frameworks 5
Conflicts: qt5-qtbase-devel < 5.6.0-0.23
%if 0%{?fedora}
Requires: cmake >= 3
%endif
%if 0%{?rhel}
Requires: cmake3
%endif
%description rpm-macros
RPM macros for building KDE Frameworks 5 packages.

%package srpm-macros
Summary: RPM macros for source Qt5 packages
%description srpm-macros
%{summary}.


%install
install -Dpm644 %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.qt5-srpm

#mkdir -p %{buildroot}%{_docdir}/qt5
#mkdir -p %{buildroot}%{_docdir}/qt5-devel
#echo "- Qt5 meta package" > %{buildroot}%{_docdir}/qt5/README
#echo "- Qt5 devel meta package" > %{buildroot}%{_docdir}/qt5-devel/README

#files
#{_docdir}/qt5/README

#files devel
#{_docdir}/qt5-devel/README

#files rpm-macros
#{rpm_macros_dir}/macros.qt5

%files srpm-macros
%{rpm_macros_dir}/macros.qt5-srpm


%changelog
* Wed Nov 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.2-1
- first try, qt5-srpm-macros only (based on 5.7.0 branch)

